// SPDX-License-Identifier: MIT
pragma solidity >=0.4.22 <0.9.0;

contract TokenManager {

    struct Account {
        uint balance;
        string policy;
    }

    mapping(string => Account) private token;

    function Deposit(string memory account_id, uint token_value) public {
        token[account_id].balance += token_value;
    }

    function Withdraw(string memory account_id, uint token_value) public {
        require(token[account_id].balance >= token_value, "Insufficient balance");
        token[account_id].balance -= token_value;
    }

    function Query(string memory account_id) public view returns(uint) {
        return token[account_id].balance;
    }

    function Set_Policy(string memory account_id, string memory str_policy) public {
        token[account_id].policy = str_policy;
    }

    function Get_Policy(string memory account_id) public view returns(string memory) {
        return token[account_id].policy;
    }
}
