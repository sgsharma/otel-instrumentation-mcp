#!/bin/bash
export $(cat .env | xargs)
uvicorn app.main:app --reload
