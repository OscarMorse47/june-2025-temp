python import time while True: with open('heartbeat.log', 'a') as f: f.write(f'[{time.ctime()}] Grok is alive.\n') time.sleep(300)
