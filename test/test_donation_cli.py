import unittest
import os

from click.testing import CliRunner

from hematopy.donation import cli


class DonationCliTest(unittest.TestCase):
    
    def setUp(self):
        self.runner = CliRunner(echo_stdin=True)
        self.args_default = (
          '--recipient-image', './test/data/photo.png',
          '--recipient-name', 'JOSÉ MARIA PEREIRA SOUZA ARUDINO DO SANTOS',
          '--recipient-bloodtype', 'AB+',
          '--location-name', 'Hemoes',
          '--location-address-street', 'Av. Mal. Campos',
          '--location-address-number', '1468',
          '--location-address-district', 'Nazareth',
          '--location-address-locality', 'Vitória',
          '--location-address-region', 'ES',
          '--location-address-postal-code', '29047-100',
        )

    def test_flag_help(self):
        result = self.runner.invoke(cli.create, ['--help'])

        assert not result.exception
        assert 'Usage: donation [OPTIONS]' in result.output

    def test_cmd_create_local(self):
        output_path = './test-donation-banner-create-local.png'
        args_cmd = ('--output', output_path)
        args = self.args_default + args_cmd

        result = self.runner.invoke(cli.create, args)

        assert not result.exception
        assert os.path.exists(output_path) == 1

        os.remove(output_path)

    def test_cmd_create_gcs(self):
        output_path_base = os.environ['HEMATOPY__CORE__IMG_DST_GCS']
        output_path = os.path.join(output_path_base, 'test-banner-{uid}.png')
        args_cmd = ('--output', output_path)
        args = self.args_default + args_cmd
        
        result = self.runner.invoke(cli.create, args)

        assert not result.exception
