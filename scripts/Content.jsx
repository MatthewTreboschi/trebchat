    
import * as React from 'react';


import { Button } from './Button';
import { Socket } from './Socket';

export function Content() {
    const [messages, setMessages] = React.useState([]);
    
    function getNewMessages() {
        React.useEffect(() => {
            Socket.on('messages received', (data) => {
                setMessages(data['allMessages']);
                console.log("Received messages form server: " + data['allMessages']);
            })
            //Socket.on('messages received', updateMessages);
            //return () => {
            //    Socket.off('messages received', updateMessages);
            //}
        });
    }
    
    function updateMessages(data) {
        console.log("Received messages from server: " + data['allMessages']);
        setMessages(data['allMessages']);
    }
    
    getNewMessages();

    return (
        <div>
            <h1>TrebChat Messages!</h1>
                <dl>
                    {
                        messages.map(
                        (message, index) => <dt key={index}>{message}</dt>)
                    }
                </dl>
            <Button />
        </div>
    );
}
