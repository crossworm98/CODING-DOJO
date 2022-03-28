import React from 'react';

const Boxy = (props) => {
    const colorstyle = {
        backgroundColor: props.color
    }
    return (
        <div class="boxy">
            <h1 class="boxy2" style={colorstyle} ></h1>
        </div>
    );
};


export default Boxy;
