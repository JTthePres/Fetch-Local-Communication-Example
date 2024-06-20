# Fetch-Local-Communication-Example
A simply example of local communication between two agents of fetch.ai blockchain in the same script.

## Description:
In this example there are two agents (*Dante* and *Virgilio*) that firstly at the startup each of them execute an hello function for showing in console their address and name.

Then Virglio, who is the sender, sends every 3.0s a mex with a field **"message"** with a fixed content and another field **"value"** with a random integer value.

Dante, that is the receiver, has an handler for the incoming messages for showing them in console.

## Tecnology:
I've use the **uAgents framework** written for python by fetch.ai itself.
