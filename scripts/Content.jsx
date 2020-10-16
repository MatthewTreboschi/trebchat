    
import * as React from 'react';


import { Button,NameInput} from './Button';

import { Socket } from './Socket';

export function Content() {
    const [messages, setMessages] = React.useState([]);
    const [names, setNames] = React.useState([]);
    const [count, setCount] = React.useState([]);
    
    function getNewMessages() {
        React.useEffect(() => {
            Socket.on('messages received', (data) => {
                setMessages(data['allMessages']);
                setNames(data['allNames']);
                console.log("Received messages form server: " + data['allMessages']);
            })
            Socket.on('connected', (c) => {
                setCount(c['connectCount']);
            })
        });
    }
    
    function updateMessages(data) {
        console.log("Received messages from server: " + data['allMessages']);
        setMessages(data['allMessages']);
    }
    
    getNewMessages();

    return (
        <div id="main">
            <div>
                <h1 id="logo">TrebChat Messages!</h1>
                <h3 id="pop">TrebChat Nation Population: { count }</h3>
                <NameInput id="navig"/>
            </div>
            <div>
                <table>
                    <thead>
                        <tr>
                            <th id="namecol">username</th>
                            <th id="messagecol">message</th>
                        </tr>
                    </thead>
                    <tbody>
                        {
                        messages.map(
                        (message, index) => 
                        <tr key={index}>
                            <td id="namecol">{names[index]}</td>
                            <td>{message}</td>
                        </tr>)
                        }
                    </tbody>
                </table>
            </div>
            <Button />
        </div>
    );
}
