import click
from tqdm import tqdm
from time import sleep
from subprocess import call

@click.command()
@click.argument('time')
@click.option("--unit", type=click.Choice(["second", "minute", "hour"]), default="second")
def main(time, unit):
  unit_switch = {
    "second": 1,
    "minute": 60,
    "hour": 3600
  }
  time = int(time)*unit_switch.get(unit)
  for i in tqdm(range(time)):
    sleep(1)
  call(["notify-send", "Time's up!"])

if __name__ == "__main__":
    main()
