import React, { useState } from 'react';

const ColorForm = (props) => {
    const { setColors } = props
    const [color, setColor] = useState("")
    const createBox = (event) => {
        event.preventDefault();
        console.log(color)
        setColors(colors => [...colors, color ])
        // console.log("You made a box with color", newBox);
    };

    return (
        <><form onSubmit={event => createBox(event)}>
            <div>
                <label>Color</label>
                <input type="color" onChange={event => setColor(event.target.value)}/>
            </div>
            <input type="submit" value="Submit"/>
        </form>
        <h1></h1>
        </>

    );
}



export default ColorForm;

