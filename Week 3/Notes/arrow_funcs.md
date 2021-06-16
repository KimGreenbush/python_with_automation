# Arrow Functions
Arrow functions, introduced in ES6, provides a **concise way to write functions** in JavaScript. They **save developers time and simplify function scope**.

- **One-line arrow functions** have **implict return** and defined **without curly braces**.

```js
let func = (arg1, arg2, ...argN) => expression;

var hello = () => "Hello World!";
hello(); // output: "Hello World!"
```

- **Multiline arrow functions** have multiple statements inside the function, **enclosed with curly braces** and **need an explicit return** to return something.

```js
let func = (arg1, arg2, ...argN) =>{
stament1;
...
statementn;
return value;
}

var sum = (a, b) => {
      let result =  a + b;
    return "Sum is" + result;
};

sum(5, 3);  //output: "sum is 8"
```