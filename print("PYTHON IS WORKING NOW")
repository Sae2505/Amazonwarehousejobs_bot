name: Amazon Job Bot

on:
  workflow_dispatch:

jobs:
  run:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.10'

      - name: Install requests
        run: pip install requests

      - name: Show files (DEBUG)
        run: ls -al

      - name: Run bot
        env:
          BOT_TOKEN: ${{ secrets.BOT_TOKEN }}
          CHAT_ID: ${{ secrets.CHAT_ID }}
        run: |
          echo "STARTING PYTHON"
          python main.py
