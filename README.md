# 🚁 Drone Operations Coordinator AI

An AI-powered assistant that automates drone mission coordination including pilot matching, drone allocation, conflict detection, and emergency reassignment.

## Features

* Pilot availability search
* Smart mission assignment
* Conflict detection (maintenance, availability)
* Urgent reassignment
* Real-time Google Sheets synchronization
* Conversational interface

## Architecture

User → Chat UI → Intent Parser → Rule Engine → Google Sheets Database

## Tech Stack

Python, Streamlit, Pandas, Google Sheets API, NLP Intent Parsing

## Example Commands

find mapping pilot in bangalore
assign mapping mission in bangalore
urgent replace mission in bangalore

## Running Locally

pip install -r requirements.txt
python -m streamlit run app.py
