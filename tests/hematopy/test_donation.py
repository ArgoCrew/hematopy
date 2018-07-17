CONSOLE_SCRIPT_NAME = 'hematopy'

def test_cli_help(script_runner):
    must_have = ('Usage: hematopy [OPTIONS] COMMAND [ARGS]...')
    ret = script_runner.run('hematopy', '--help')
    
    assert ret.success
    assert must_have[0] in ret.stdout
    assert ret.stderr == ''