/**
 * Truffle configuration file
 * Used to configure networks and Solidity compiler
 */

module.exports = {

  networks: {

    // Local development network (Ganache)
    development: {
      host: "127.0.0.1",     // Localhost
      port: 8545,            // Ganache default port
      network_id: "*"        // Match any network id
    }

  },

  // Configure Solidity compiler
  compilers: {
    solc: {
      version: "0.8.20",     // Solidity compiler version
      settings: {
        optimizer: {
          enabled: true,
          runs: 200
        }
      }
    }
  }

};
