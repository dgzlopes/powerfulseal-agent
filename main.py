from fastapi import FastAPI
from pydantic import BaseModel

from enum import Enum, auto
from typing import List
import asyncio
import time
import logging

from fastapi_utils.session import FastAPISessionMaker
from fastapi_utils.tasks import repeat_every

from resource import ResourceAttack
from network import NetworkAttack
from state import StateAttack

app = FastAPI(
    title="Powerfulseal-agent",
    description="Nothing fancy, just a proof of concept.",
    version="0.0.1",
)

logger = logging.getLogger("api")

attack_list = []


def build(config):
    if config.command.type in ("cpu", "memory"):
        new_attack = ResourceAttack(
            config.command.type, config.command.args, config.target
        )
    elif config.command.type in ("latency"):
        new_attack = NetworkAttack(
            config.command.type, config.command.args, config.target
        )
    elif config.command.type in ("shutdown","restart"):
        new_attack = StateAttack(
            config.command.type, config.command.args, config.target
        )
    attack_list.append(new_attack)
    return new_attack.run()


class AttackType(str, Enum):
    cpu = "cpu"
    memory = "memory"
    latency = "latency"
    shutdown = "shutdown"
    restart = "restart"


class Command(BaseModel):
    type: AttackType
    args: List[str] = []


class AttackConfig(BaseModel):
    command: Command


@app.on_event("startup")
@repeat_every(seconds=5)
def attack_cleaner():
    for index, attack in enumerate(attack_list):
        attack.duration -= 5
        if attack.duration < 0:
            attack.remove()
            attack_list.pop(index)


@app.on_event("startup")
def on_first_run():
    logger.warning("Cleaning past attacks")

@app.get("/")
def default():
    '''
        Default message.
    '''
    return {"message": "Powerfulseal-Agent POC"}

@app.get("/attacks")
def list_all_attacks():
    '''
        List all attacks.
    '''
    return {"attacks": attack_list}


@app.get("/attacks/{attack_id}")
def list_specific_attack(attack_id: str):
    '''
        List a specific attack.
    '''
    for attack in attack_list:
        if str(attack.id) == attack_id:
            return {"removed": attack}

    return {"message": "not found"}


@app.delete("/attacks")
def delete_all_active_attacks():
    '''
        Delete all existing attacks.
    '''
    for attack in attack_list:
        attack.remove()
    attack_list.clear()
    return {"removed": "all attacks"}


@app.delete("/attacks/{attack_id}")
def delete_specific_attack(attack_id: str):
    '''
        Delete one specific attack.
    '''
    for index, attack in enumerate(attack_list):
        if str(attack.id) == attack_id:
            attack.remove()
            attack_list.pop(index)
            break

    return {"removed": attack_id}


@app.post("/attacks/new")
def create_new_attack(attack: AttackConfig):
    '''
        Create a new attack.
    '''
    return {"running": build(attack)}
