import os


cli_args_default = (
  '--recipient-image', './tests/data/photo.png',
  '--recipient-name', 'JOSÉ MARIA PEREIRA SOUZA ARUDINO DO SANTOS',
  '--recipient-blood-type', 'AB+',
  '--location-name', 'Hemoes',
  '--location-address-street', 'Av. Mal. Campos',
  '--location-address-number', '1468',
  '--location-address-district', 'Nazareth',
  '--location-address-locality', 'Vitória',
  '--location-address-region', 'ES',
  '--location-address-postal-code', '29047-100',
)

def test_cli_flag_help(script_runner):
    must_have = ('Usage: hematopy [OPTIONS] COMMAND [ARGS]...')
    ret = script_runner.run('hematopy', '--help')
    
    assert ret.success
    assert must_have[0] in ret.stdout
    assert ret.stderr == ''

def test_cli_command_create_local(script_runner):
    arg_output = './tests/test-donation-cli-command-create.png'
    ret = script_runner.run('hematopy', 'create', 'donation', 
                            '--output', arg_output,
                            *cli_args_default)
    assert ret.success
    assert ret.stderr == ''
    assert os.path.exists(arg_output)

    os.remove(arg_output)

def test_cli_command_create_gcs(script_runner):
    arg_output_path = os.environ['HEMATOPY__CORE__IMG_DST_GCS']
    arg_output = os.path.join(arg_output_path, 'test-banner-{uid}.png')
    
    ret = script_runner.run('hematopy', 'create', 'donation', 
                            '--output', arg_output,
                            *cli_args_default)
    assert ret.success
    assert ret.stderr == ''
