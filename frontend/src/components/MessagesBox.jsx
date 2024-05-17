import React, {useState} from 'react';
import useChatStore from '../store/chatStore';
import { RiRobot3Line } from "react-icons/ri";
import { PiFinnTheHuman } from "react-icons/pi";



const MessagesBox = () => {
    const messages = useChatStore((state) => state.messages)
    return (
        <div>
        {messages.map((message, index) => (
            
            index%2!=0 
            ?
            <div key={index} className="flex p-2 bg-red-400 my-5 rounded-xl">
              <div className="mx-2 my-auto"><RiRobot3Line /></div>
              <div className="break-all">{message}</div>
            </div>
            :
            <div key={index} className="flex p-2 bg-blue-200 my-5 rounded-xl">
              <div className="mx-2 my-auto"><PiFinnTheHuman /></div>
              <div className="break-all">{message}</div>
            </div>
            
            ))}
        </div>
    )
}

export default MessagesBox