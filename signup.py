#!d:\Python34\python.exe
print("""
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Signup</title>
        <link href="css/bootstrap.css" rel="stylesheet">
        <link href="css/style.css" rel="stylesheet">
        <script src="js/jquery.js"></script>
        <script src="js/bootstrap.min.js"></script>
    </head>
    <body>
        <div class="navbar navbar-inverse navbar-fixed-top">
            <div class="container">
                <div class="navbar-header">
                    <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#myNavbar">
                        <span class="icon-bar"></span>
                        <span class="icon-bar"></span>
                        <span class="icon-bar"></span>                        
                    </button>
                    <a class="navbar-brand" href="mains.py">College Achievements</a>
                </div>
                <div class="collapse navbar-collapse" id="myNavbar">
                    <ul class="nav navbar-nav navbar-right">
                        <li><a href="signup.py"><span class="glyphicon glyphicon-user"></span> Sign Up</a></li>
                    </ul>
                </div>
            </div>
        </div>
        <div class="container-fluid decor_bg" id="content">
            <div class="row">
                <div class="container">
                    <div class="col-lg-4 col-lg-offset-4 col-md-6 col-md-offset-3">
                        <h2>SIGN UP</h2>
                        <form  action="regisdb.py" method="get">
                            <div class="form-group">
                                <input class="form-control" placeholder="Fisrt Name" name="t1"  required>
                            </div>
                            <div class="form-group">
                                <input class="form-control" placeholder="Second Name" name="t2"  required>
                            </div>
                            <div class="form-group">
                                <input type="email" class="form-control"  placeholder="Email"  name="t3" required>
                            </div>
                            <div class="form-group">
                                <input type="text" class="form-control"  placeholder="Branch" name="t4" required>
                            </div>
                               <div class="form-group">
                                <input type="text" class="form-control"  placeholder="Student/Teacher" name="t7" required>
                            </div>
                            <div class="form-group">
                                <input  type="text" class="form-control"  placeholder="Year" name="t5" required>
                            </div>
                            <div class="form-group">
                                <input  type="text" class="form-control"  placeholder="Achievement" name="t6" required>
                            </div>
                            <button type="submit" name="a2" class="btn btn-primary">Submit</button>
                        </form>
                    </div>
                </div>
            </div>
        </div>
        <footer>
            <div class="container">
                <center>
                    <p>Copyright &copy;College Achievements. All Rights Reserved  |  Contact Us:+91 94307 73356</p>	
                </center>
            </div>
        </footer>
    </body>
</html>
""")
