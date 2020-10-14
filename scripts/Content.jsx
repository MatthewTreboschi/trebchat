    
import * as React from 'react';


import { Button } from './Button';
import { Socket } from './Socket';

export function Content() {
    const [addresses, setAddresses] = React.useState([]);
    
    function getNewAddresses() {
        React.useEffect(() => {
            Socket.on('addresses received', (data) => {
                setAddresses(data['allAddresses']);
                console.log("Received addresses form server: " + data['allAddresses']);
            })
            //Socket.on('addresses received', updateAddresses);
            //return () => {
            //    Socket.off('addresses received', updateAddresses);
            //}
        });
    }
    
    function updateAddresses(data) {
        console.log("Received addresses from server: " + data['allAddresses']);
        setAddresses(data['allAddresses']);
    }
    
    getNewAddresses();

    return (
        <div>
            <h1>USPS Addresses!</h1>
                <dl>
                    {
                        addresses.map(
                        (address, index) => <dt key={index}>{address}</dt>)
                    }
                </dl>
            <Button />
        </div>
    );
}
