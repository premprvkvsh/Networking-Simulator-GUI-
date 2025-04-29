# **COMPUTER NETWORKING SIMULATOR**

The project Networking simulator GUI is from computer Networks. This simulator currently is capable of demonstrating the message transmission between different end devices in the domain of Data link layer. It shows exact simuation of the flow and access control protocols.

https://user-images.githubusercontent.com/73434283/117675552-4a1f2f80-b1ca-11eb-9bd2-ff7b9f5e8d55.mp4

<p>
  <em> Short clip demonstrating how to make connections and show message transmission between two end devices. Here all the five devices are connected to a hub and the sender is the device 3 and device 2 is the receiver. Stop and wait ARQ is being used. </em>
</p>

## Programming Languages used:

1. HTML5
2. CSS3
3. Vanilla Javascript(with Es6 modules)

## SETUP:

1. Install a latest Text editor like VsCode on your system.
2. Install a live server.
3. Open the folder using VsCode and run the simulator on a live server.

make_connection.js : import {list_devices, End_device, reset_devices} from './Device.js';
import {list_hubs, Hub, reset_hubs} from './Hub.js';
import {list_switches, Switch, reset_switches, } from './Switch.js';
import {list_bridges, Bridge, reset_bridges} from './Bridge.js';
//import {reset_log} from './main.js';
//import {reset_tokken} from './Message_Transmission.js';

    export function make_connection_device_to_device()     // device to device connection
            {
                if(arguments[0] >= list_devices.length  || arguments[1] >= list_devices.length)
                {
                    return "invalid";
                }

                var d1 = list_devices[arguments[0]];
                var d2 = list_devices[arguments[1]];

                var x = d1.is_port_vacant();
                var y = d2.is_port_vacant();

                if(x && y)
                {
                    d1.port[0] = d2.get_mac_address();
                    d2.port[0] = d1.get_mac_address();
                    return "success";
                }

                else
                {
                    return "no port";
                }
            }

    export function make_connection_hub_to_device()    // hub to device connection
            {
                if(arguments[0] >= list_hubs.length || arguments[1] >= list_devices.length)
                {
                    return "invalid";
                }

                var h = list_hubs[arguments[0]];
                var d = list_devices[arguments[1]];

                var x = d.is_port_vacant();
                var y = h.is_hport_vacant();

                if(x && y)
                {
                    for(var i = 0; i < h.ports.length; i++)
                    {
                        if(h.ports[i] == "-1")
                        {
                            h.ports[i] = d.get_mac_address();
                            break;
                        }
                    }
                    d.port[0] = h.serial;
                    return "success";
                }

                else
                {
                    return "no port";
                }
            }

    export function make_connection_switch_to_device()    // switch to device connection
            {
                if(arguments[0] >= list_switches.length || arguments[1] >= list_devices.length)
                {
                    return "invalid";
                }

                var s = list_switches[arguments[0]];
                var d = list_devices[arguments[1]];

                var x = d.is_port_vacant();
                var y = s.is_port_vacant();

                if(x && y)
                {
                    for(var i = 0; i < s.ports.length; i++)
                    {
                        if(s.ports[i] == "-1")
                        {
                            s.ports[i] = d.get_mac_address();
                            break;
                        }
                    }
                    d.port[0] = s.serial;
                    return "success";
                }

                else
                return "no port";
            }

    export function connect_device_to_left()   // connect device to left segment
            {
                if(arguments[0] >= list_bridges.length || arguments[1] >= list_devices.length)
                {
                    return "invalid";
                }

                var b = list_bridges[arguments[0]];
                var d = list_devices[arguments[1]];

                if(!d.is_port_vacant() || !b.is_ls())
                {
                    return "no port";
                }

                d.port[0] = b.serial;
                for(var i = 0; i < b.left_segment.length; i++)
                {
                    if(b.left_segment[i] == "-1")
                    {
                        b.left_segment[i] = d.get_mac_address();
                        return "success";
                    }
                }
            }

    export function connect_device_to_right()   // connect device to right segment
            {
                if(arguments[0] >= list_bridges.length || arguments[1] >= list_devices.length)
                {
                    return "invalid";
                }

                var b = list_bridges[arguments[0]];
                var d = list_devices[arguments[1]];

                if(!d.is_port_vacant() || !b.is_rs())
                {
                    return "no port";
                }

                d.port[0] = b.serial;
                for(var i = 0; i < b.right_segment.length; i++)
                {
                    if(b.right_segment[i] == "-1")
                    {
                        b.right_segment[i] = d.get_mac_address();
                        return "success";
                    }
                }
            }

    export  function make_connection_hub_to_switch()
            {
                if(arguments[0] >= list_hubs.length || arguments[1] >= list_switches.length)
                {
                    return "invalid";
                }
                var h = list_hubs[arguments[0]];
                var s = list_switches[arguments[1]];

                var x = h.is_hport_vacant();
                var y = s.is_port_vacant();

                if(x && y)
                {
                    for(var i = 0; i < h.ports.length; i++)
                    {
                        if(h.ports[i] == "-1")
                        {
                            h.ports[i] = s.serial;
                            break;
                        }
                    }
                    for(var i = 0; i < s.ports.length; i++)
                    {
                        if(s.ports[i] == "-1")
                        {
                            s.ports[i] = h.serial;
                            break;
                        }
                    }

                    return "success";
                }

                else
                {
                    return "no port";
                }

            }

    export  function switch_to_switch()
            {
                if(Math.max(arguments[0], arguments[1]) >= list_switches.length)
                {
                    return "invalid";
                }

                var s1 = list_switches[arguments[0]];
                var s2 = list_switches[arguments[1]];

                var x = s1.is_port_vacant();
                var y = s2.is_port_vacant();

                if(x && y)
                {
                    for(var i = 0; i < s1.ports.length; i++)
                    {
                        if(s1.ports[i] == "-1")
                        {
                            s1.ports[i] = s2.serial;
                            break;
                        }
                    }

                    for(var i = 0; i < s2.ports.length; i++)
                    {
                        if(s2.ports[i] == "-1")
                        {
                            s2.ports[i] = s1.serial;
                            return "success";
                        }
                    }
                }

                return "no port";
            }

    export  function reset()
            {
                reset_switches();
                reset_hubs();
                reset_bridges();
                reset_devices();
                //reset_log();
                //reset_tokken();
            }

remove_connection.js : import {list_devices, End_device} from './Device.js';
import {list_hubs, Hub} from './Hub.js';
import {list_switches, Switch} from './Switch.js';
import {list_bridges, Bridge} from './Bridge.js';

        // remove connection from one end device to another end device

    export function remove_connection_end_to_end()
            {
                if(Math.max(arguments[0], arguments[1]) >= list_devices.length)
                {
                    return "invalid";
                }

                var d1 = list_devices[arguments[0]];
                var d2 = list_devices[arguments[1]];

                if(d1.port[0] != d2.get_mac_address() || d2.port[0] != d1.get_mac_address())
                {
                    return "no connection";
                }

                d1.port[0] = "-1";
                d2.port[0] = "-1";
                return "success";
            }

            // remove connection between an end device and a hub

    export  function remove_connection_hub_to_end()
            {
                if(arguments[0] >= list_hubs.length || arguments[1] >= list_devices.length)
                {
                    return "invalid";
                }
                var h = list_hubs[arguments[0]];
                var d = list_devices[arguments[1]];

                if(d.port[0] != h.serial)
                {
                    return "no connection";
                }

                var add = d.get_mac_address();

                for(var i = 0; i < h.ports.length; i++)
                {
                    if(h.ports[i] == add)
                    {
                        h.ports[i] = "-1";
                        break;
                    }
                }

                d.port[0] = "-1";
                return "success";
            }

            // Remove connection between a bridge and a device

    export  function remove_connection_bge_to_device()
            {
                if(arguments[0] >= list_bridges.length || arguments[1] >= list_devices.length)
                {
                    return "invalid";
                }

                var b = list_bridges[arguments[0]];
                var d = list_devices[arguments[1]];

                if(d.ports[0] != b.serial)
                {
                    return "no connection";
                }

                var add = d.get_mac_address();

                //search in left

                for(var i = 0; i < b.left_segment.length; i++)
                {
                    if(b.left_segment[i] == add)
                    {
                        b.left_segment[i] = "-1";
                        d.ports[0] = "-1";
                        return "success";
                    }
                }
                    // search in right

                for(var i = 0; i < b.right_segment.length; i++)
                {
                    if(b.right_segment[i] == add)
                    {
                        b.right_segment[i] = "-1";
                        d.ports[0] = "-1";
                        return "success";
                    }
                }
            }

            // remove connection between hub and switch

    export   function remove_connection_hub_to_swt()
            {
                if(arguments[0] >= list_hubs.length || arguments[1] >= list_switches.length)
                {
                    return "invalid";
                }
                var h = list_hubs[arguments[0]];
                var s = list_switches[arguments[1]];

                var check1 = 0,check2 = 0;
                var m;
                for(var i = 0; i < h.ports.length; i++)
                {
                    if(h.ports[i] == s.serial)
                    {
                        check1=1;
                        m = i;
                        break;
                    }
                }
                for(var i = 0; i < s.ports.length; i++)
                {
                    if(s.ports[i] == h.serial)
                    {
                        check2=1;
                        break;
                    }
                }
                if(!check1 || !check2)
                {
                    return "no connection";
                }
                if(s.ports[0] == h.serial)
                {
                    for(var i = 0; i < s.left_table.length; i++)
                    {
                        s.left_table[i] = "-1";
                    }

                    s.ports[0] = "-1";
                }
                else
                {
                    for(var i = 0; i < s.right_table.length; i++)
                    {
                        s.right_table[i] = "-1";
                    }
                    s.ports[1] = "-1";
                }

                h.ports[m] = "-1";
                return "success";
            }

            // remove connection between a device and a switch

    export  function remove_connection_switch_to_end()
            {
                if(arguments[0] >= list_switches.length || arguments[1] >= list_devices.length)
                {
                    return "invalid";
                }
                var s = list_switches[arguments[0]];
                var d = list_devices[arguments[1]];

                if(d.port[0] != s.serial)
                {
                   return "no connection";
                }

                var add = d.get_mac_address();

                for(var i = 0; i < s.ports.length; i++)
                {
                    if(s.ports[i] == add)
                    {
                        s.ports[i] = "-1";
                        s.table[i] = "-1";
                        break;
                    }
                }

                d.port[0] = "-1";
                return "success";
            }.

style.css : h1{
color: purple;
text-align: center;
font-size: 50px;
}

h2
{
color:yellow;
text-align: center;
margin-top: 4%;
font-size: 30px;
}

h3
{
color:white;
font-size: 20px;
}

h4
{
color: black;
font-size: 20px;
text-align: center;
}

.options
{
width: 40%;
height: auto;
margin: auto;
display: flex;
margin-top: 2%;

}

.btn{
background-color: black;
color: whitesmoke;
font-size: 20px;
border: 1;
border-color: lightseagreen;
width: 20%;
height: 70px;
display: inline-block;
text-align: center;
transition-duration: 0.3s;
border-radius: 5px;
padding-top: 2%;
padding-bottom: 4%;
margin-right: 8%;
display: list-item;
margin-top: 10%;

}

.btn:hover{
background-color: black;
color: white;
border-color: red;
}

body
{

    background-image: url("3.png");

}

.values
{
width: 40%;
height: auto;
display: flex;
text-align: center;
padding-bottom: 1%;
padding-top: 3%;
padding-right: 4.7%;
margin: auto;

}

.counter
{
text-align: center;
margin: auto;
font-size: 25px;
color: yellow;
}

.connection
{
height: auto;
display: flex;
margin: auto;
text-align: center;
padding-bottom: 0.5%;
padding-top: 0.5%;
padding-right: 4.7%;
}

.d2d
{
margin: auto;
display: inline-block;
width: 60%;

}

.con
{
width: 50%;
text-align: center;
font-size: 14px;
min-width: fit-content;
}

.make_connection
{
text-align: center;
background-color: black;
color: whitesmoke;
border: 1;
border-color: lightseagreen;
text-align: center;
transition-duration: 0.3s;
border-radius: 5px;
margin: auto;
font-size: 18px;
min-width: fit-content;
}

.make_connection:hover
{
background-color: black;
color: white;
border-color: red;
}

#CD
{
padding-top: 7%;
background-color: inherit;
margin: auto;
display: flex;
width: 40%;
}

#CD_button
{
text-align: center;
background-color: rgb(34, 34, 151);
color: whitesmoke;
border: 1;
border-color: lightseagreen;
text-align: center;
transition-duration: 0.3s;
border-radius: 5px;
margin: auto;
font-size: 18px;
max-width: fit-content;
padding-top: 2%;
padding-bottom: 2%;
}

#CD_button:hover
{
color: white;
animation: ease-out;
border-radius: 3%;
border-color: red;
}

.reset
{
padding-top: 2%;
padding-bottom: 1%;
background-color:inherit;
margin: auto;
display: flex;
width: 70%;
}

#reset_button
{
text-align: center;
background-color: rgb(34, 34, 151);
color: whitesmoke;
border: 1;
border-color: lightseagreen;
text-align: center;
transition-duration: 0.3s;
border-radius: 5px;
font-size: 17px;
width: 5%;
min-width: fit-content;
padding-top: 1%;
padding-bottom: 1%;
max-height:fit-content;
float:right;
position: absolute;
top: 1%;
right: 1%;
}

#reset_button:hover
{
background-color: rgb(53, 53, 212);
color: white;
animation: ease-out;
border-radius: 3%;
border-color: red;
}

.fc_text
{
color: violet;
}

.radio_button
{
margin-left: 7%;
}

.send
{
margin-left: 7%;
margin-top: 1%;
width: 3.5%;
min-width: fit-content;
background-color:green;
border-color: lightseagreen;
font-size: 17px;
font-weight: bold;
min-height: fit-content;
color: linen;
}

.log
{
float: right;
display: inline;
background-color: white;
height: 400px;
width: 25%;
overflow: scroll;
word-wrap: break-word;
padding-left: 1%;
padding-right: 1%;
}

.send:hover
{
background-color: rgb(48, 131, 48);
}

- {
  font-family: 'Times New Roman', Times, serif;
  } switch.js : export var C_switch = 1;
  export var list_switches = [];
  list_switches.push(-1);

      export class Switch
          {
              constructor()
              {
                  this.ports = ["-1", "-1", "-1", "-1", "-1", "-1", "-1","-1", "-1", "-1", "-1", "-1", "-1", "-1"];
                  this.table = ["-1", "-1", "-1", "-1", "-1", "-1", "-1","-1", "-1", "-1", "-1", "-1", "-1", "-1"];
                  this.serial = C_switch + 999;
                  this.left_table = ["-1", "-1", "-1", "-1", "-1", "-1"];
                  this.right_table = ["-1", "-1", "-1", "-1", "-1", "-1"];
                  C_switch ++;
              }

              is_port_vacant()
              {
                  for(var i = 0; i < this.ports.length; i++)
                  {
                      if(this.ports[i] == "-1")
                      {
                          return 1;
                      }
                  }
                  return 0;
              }
          }


        export function create_switch()
          {
              let s = new Switch();
              list_switches.push(s);
          }

      export function reset_switches()
      {
          list_switches = ["-1"];
          C_switch = 1;
      }

  finally all files done. now take time and tell me step by step file by file guide to make changes and make the project intereactive. thanks
