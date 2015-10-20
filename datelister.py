import click
import arrow

DEFAULT_DAYS = 7

def parsedate(datestr, default):
    if datestr is None:
        return default
    try:
        dt = arrow.get(datestr)
    except:
        raise click.ClickException("Couldn't parse date '%s'" % datestr)
    else:
        return dt

@click.command()
@click.option('--frame', '-r', default='day')
@click.option('--start', '-s')
@click.option('--end', '-e')
@click.option('--format', '-f', 'formatstr', default='ddd MMM D')
def cli(frame, start, end, formatstr):
    """Print a sequence of dates"""
    start = parsedate(start, arrow.now())
    end = parsedate(end, start.replace(days=DEFAULT_DAYS))

    for r in arrow.Arrow.range(frame, start, end):
        click.echo(r.format(formatstr))