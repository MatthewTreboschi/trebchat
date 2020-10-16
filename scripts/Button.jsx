import * as React from 'react';
import { Socket } from './Socket';

function messageSubmit(event) {
    let newMessage = document.getElementById("message_input");
    Socket.emit('new message input', {
        'message': newMessage.value
    });
    console.log('Sent the message ' + newMessage.value + ' to server!');
    newMessage.value = ''
    
    event.preventDefault();
}

export function Button() {
    return (
        <form onSubmit={messageSubmit}>
            <input id="message_input" placeholder="Enter a Message:"></input>
            <button>Send</button>
        </form>
    );
}

function nameSubmit(event) {
    let newName = document.getElementById("name_input");
    Socket.emit('new name input', {
        'name': newName.value
    });
    console.log('Sent the message ' + newName.value + ' to server!');
    newName.value = ''
    
    event.preventDefault();
}

export function NameInput() {
    return (
        <form onSubmit={nameSubmit}>
            <input id="name_input" maxLength="12" placeholder="Make a name!"></input>
            <button>Change name!</button>
        </form>)
}
