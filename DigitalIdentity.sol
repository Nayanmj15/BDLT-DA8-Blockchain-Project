// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract DigitalIdentity {
    struct User {
        uint userId;
        string name;
        string department;
        address wallet;
    }

    mapping(address => User) private users;
    mapping(address => bool) private registered;

    uint public totalUsers;

    function register(
        uint _userId,
        string memory _name,
        string memory _department
    ) public {
        require(_userId > 0, "User ID must be greater than zero");
        require(!registered[msg.sender], "Wallet already registered");

        users[msg.sender] = User(
            _userId,
            _name,
            _department,
            msg.sender
        );

        registered[msg.sender] = true;
        totalUsers++;
    }

    function getUser(address _wallet)
        public
        view
        returns (uint, string memory, string memory, address)
    {
        User memory u = users[_wallet];
        return (u.userId, u.name, u.department, u.wallet);
    }

    function isRegistered(address _wallet)
        public
        view
        returns (bool)
    {
        return registered[_wallet];
    }
}
