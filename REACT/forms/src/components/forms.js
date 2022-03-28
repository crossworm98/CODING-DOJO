import React, { useState } from 'react';





const UserForm = (props) => {
    const [firstname, setFirstname] = useState("");
    const [firstnameError, setFirstnameError] = useState("");
    const [lastname, setLastname] = useState("");
    const [lastnameError, setLastnameError] = useState("");
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [confirmpassword, setConfirmpassword] = useState("");

    const createUser = (e) => {
        e.preventDefault();
        const newUser = { firstname, lastname, email, password };
        console.log("Welcome", newUser);
    };
    const firstnameHandler = (event) => {
        setFirstname(event.target.value);

        if(event.target.value.length < 3){
            setFirstnameError("First name needs at least 3 characters");
        }
        else{
            setFirstnameError("");
        }
    }
    const lastnameHandler = (event) => {
        setLastname(event.target.value);

        if(event.target.value.length < 3){
            setLastnameError("Last name needs to be at least 3 characters");
        }
        else{
            setLastnameError("");
        }
    }
    return (
        <><form onSubmit={createUser}>
            <div>
                <label>First Name: </label>
                <input type="text" onChange={firstnameHandler} />
                <span className="alert-danger">{firstnameError}</span>
            </div>
            <div>
                <label>Last Name: </label>
                <input type="text" onChange={lastnameHandler} />
                <span classname="alert-danger">{lastnameError}</span>
            </div>
            <div>
                <label>Email Address: </label>
                <input type="text" onChange={(e) => setEmail(e.target.value)} />
                {email.length < 10 && email.length > 0 ? "Email must be at least 10 characters" : ""}
            </div>
            <div>
                <label>Password: </label>
                <input type="text" onChange={(e) => setPassword(e.target.value)} />
                {password.length < 5 && password.length > 0 ? "Password must be at least 3 characters" : ""}
            </div>
            <div>
                <label>Confirm Password: </label>
                <input type="text" onChange={(e) => setConfirmpassword(e.target.value)} />
                {password != confirmpassword ? "Passwords must match" : ""}
            </div>
            <input type="submit" value="Create User" />
        </form>
        <h1></h1>
        </>

    );

};

export default UserForm;
