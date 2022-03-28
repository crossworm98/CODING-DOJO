import React, { Component} from 'react';

class People extends Component{
    constructor(props) {
        super(props);
        console.log(props)
    }
    
    render(){
    return(
        <div>
            <h1>{this.props.info.name}</h1>
            <p>Height: {this.props.info.height}</p>
            <p>Mass: {this.props.info.mass}</p>
            <p>Hair Color: {this.props.info.hair_color}</p>
            <p>Skin Color: {this.props.info.skin_color}</p>
            <p>{this.props.children}</p>

        </div>
    );
    }
}

export default People;