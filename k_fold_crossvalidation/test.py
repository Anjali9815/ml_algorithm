from decouple import config
from sqlalchemy import create_engine
from pymongo import MongoClient
import os, sys

def create_sql_engine():
    engine = create_engine(
        f"oracle://:@",
        connect_args={
            "user": config("QM_USER"),
            "password": config("QM_PASSWORD"),
            "dsn": config("QM_DSN"),
            "config_dir": config("QM_WALLET_PATH"),
            "wallet_location": config("QM_WALLET_PATH"),
            "wallet_password": config("QM_WALLET_PASSWORD"),
        },
    ).connect()
    return engine

def create_sql_engine_uat():
    engine = create_engine(
        f"oracle://:@",
        connect_args={
            "user": config("QM_USER_UAT"),
            "password": config("QM_PASSWORD_UAT"),
            "dsn": config("QM_DSN_UAT"),
            "config_dir": config("QM_WALLET_PATH_UAT"),
            "wallet_location": config("QM_WALLET_PATH_UAT"),
            "wallet_password": config("QM_WALLET_PASSWORD_UAT"),
        },
    ).connect()
    return engine

def get_connection():
    client = MongoClient(config('QM_FR_PROD'))
    conn = client[config('QM_FRDB_PROD')]
    store = os.path.join(config("BASE_PATH"), "qm_bulk_delivery_api", "hdf5_store", "")
    # store = os.path.join(config("BASE_PATH"), "qm_bulk_delivery_api", "output", "")
    if not os.path.isdir(store):
        os.makedirs(store)
    return conn, store

def get_connection_uat():
    client = MongoClient(config('QM_FR_UAT'))
    conn = client[config('QM_FRDB_UAT')]
    store = os.path.join(config("BASE_PATH"), "qm_bulk_delivery_api", "hdf5_store", "")
    # store = os.path.join(config("BASE_PATH"), "qm_bulk_delivery_api", "output", "")
    if not os.path.isdir(store):
        os.makedirs(store)
    return conn, store

