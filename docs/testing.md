# Testing

The API client is tested using pytest. The tests are located in the `tests` directory. There are two types of tests:

- Unit tests
- End-to-end tests

## Unit tests

Unit tests are located in the `tests/unit` directory. They test the API client methods in isolation. The tests are run using the following command:

```bash
python -m pytest tests/unit
```

## End-to-end tests

End-to-end tests are located in the `tests/e2e` directory. They test the API client methods against a real Ethereum Validator client.

The tests are run using the following command:

```bash
python -m pytest tests/e2e -s
```

The e2e tests read the Validator client API endpoint and authentication token from a .env file. The file can details for one or more validators.

To run the e2e tests create a .env file in the root directory of the project with the following format:

```bash
VALIDATOR_NAME BASE_URL API_TOKEN
```

For example:

```bash
TEKU http://192.168.121.35:7500 410ef40da53b447f76ec52fa43092032
LIGHTHOUSE http://192.168.121.189:7500 api-token-0x022b0c73c4757866df53b9b24a5b254222daca269e8be677c1efb15a93aba148a7
NIMBUS http://192.168.121.42:7500 06ab97c6170c1ae09bf3eb69a300d2795fb6
LODESTAR http://192.168.121.57:7500 api-token-0x9e75d2fb89d9a8230d027665ad0f67b777aaa2f1d23f282125001d0dea753901
PRYSM http://192.168.121.53:7500 eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.e30.orijiINlQIwSlB5ZxjmzAEqlYtI3SUNC6ennFnbcVCs
```

# Testing using Ansible Molecule

The project includes a Molecule test suite that can be used to test the API client against a real Ethereum Validator client. Molecule is a testing framework for Ansible roles. The test suite is located in the `molecule` directory. The test suite uses SlingNode Ethereum Ansible roles to set up the Ethereum Validator clients. The included test suite will automatically create the .env file and output the details required by the pytest e2e tests.

See SlingNode Ethereum Ansible roles documentation for more details:

- https://docs.slingnode.com/slingnode.ethereum/
- https://docs.slingnode.com/slingnode.ethereum_node_mgmt/


Using the Molecule test suite requires working kvm/libvirt and Vagrant on the machine running the tests. For details see SlingNode Ethereum documentation page on testing https://docs.slingnode.com/slingnode.ethereum/testing

The project comes with two Molecule scenarios (test suites):

- single_validator_client
- all_validator_clients

### single_validator_client

The `single_validator_client` scenario will set up a single Ethereum Validator client. By default it will setup Lighthouse client but it can be overridden using inline environment variables as shown below.


```bash
SLINGNODE_CONSENSUS=teku SLINGNODE_VALIDATOR=teku molecule converge -s single_validator_client
```

### all_validator_clients

The `all_validator_clients` scenario will set up all Ethereum Validator clients.
