<!DOCTYPE html>
<html>
<head>
    <title>Survey Form</title>
</head>
<body>
    <h2>Survey Form</h2>
    <form method="POST">
        Name: <input type="text" name="name" required><br>
        Age: <input type="number" name="age" required><br>
        Gender: 
        <select name="gender">
            <option value="Male">Male</option>
            <option value="Female">Female</option>
        </select><br>
        Income: <input type="number" name="income" step="0.01" required><br>

        <h3>Expenses</h3>
        <label><input type="checkbox" name="utilities"> Utilities </label> 
        <input type="number" name="utilities" step="0.01"><br>
        
        <label><input type="checkbox" name="entertainment"> Entertainment </label> 
        <input type="number" name="entertainment" step="0.01"><br>

        <label><input type="checkbox" name="school_fees"> School Fees </label> 
        <input type="number" name="school_fees" step="0.01"><br>

        <label><input type="checkbox" name="shopping"> Shopping </label> 
        <input type="number" name="shopping" step="0.01"><br>

        <label><input type="checkbox" name="healthcare"> Healthcare </label> 
        <input type="number" name="healthcare" step="0.01"><br>

        <input type="submit" value="Submit">
    </form>
</body>
</html>
