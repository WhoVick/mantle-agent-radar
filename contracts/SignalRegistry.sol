// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

/// @title SignalRegistry
/// @notice Minimal Mantle Agent Radar proof contract.
/// @dev Stores hashes of off-chain alpha/risk signals so judges and users can verify timestamped agent output.
contract SignalRegistry {
    event SignalCommitted(
        bytes32 indexed signalHash,
        bytes32 indexed agentId,
        string signalType,
        uint8 confidence,
        address indexed reporter,
        uint256 timestamp
    );

    struct SignalCommitment {
        bytes32 agentId;
        string signalType;
        uint8 confidence;
        address reporter;
        uint256 timestamp;
    }

    mapping(bytes32 => SignalCommitment) public commitments;

    function commitSignal(
        bytes32 signalHash,
        bytes32 agentId,
        string calldata signalType,
        uint8 confidence
    ) external {
        require(signalHash != bytes32(0), "empty signal hash");
        require(agentId != bytes32(0), "empty agent id");
        require(confidence <= 100, "confidence > 100");
        require(commitments[signalHash].timestamp == 0, "signal already committed");

        commitments[signalHash] = SignalCommitment({
            agentId: agentId,
            signalType: signalType,
            confidence: confidence,
            reporter: msg.sender,
            timestamp: block.timestamp
        });

        emit SignalCommitted(signalHash, agentId, signalType, confidence, msg.sender, block.timestamp);
    }
}

