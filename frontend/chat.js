import {useState} from "react"
import axios from "axios"

export default function Chat(){

const [message,setMessage] = useState("")
const [response,setResponse] = useState("")

const sendMessage = async () => {

const res = await axios.post("http://localhost:8000/chat",{
message:message
})

setResponse(res.data.response)

}

return(

<div>

<h1>Campus AI Copilot</h1>

<input
value={message}
onChange={(e)=>setMessage(e.target.value)}
/>

<button onClick={sendMessage}>
Ask
</button>

<p>{response}</p>

</div>

)

}