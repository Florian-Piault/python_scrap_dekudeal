def setTemplateStart(file):
    file.write('''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    <title>Nintendo Switch Deals !</title>
</head>
<body>
    <div class="container-fluid">
''')

def setTemplateEnd(file):
    file.write(f'''</div>
    <footer class="bg-light text-center text-lg-start">
        <div class="text-center p-3" style="background-color: rgba(0, 0, 0, 0.2);">
        Scrapped from 
        <a href="https://www.dekudeals.com/" target="_blank" style="text-decoration:none; color:black">
            <strong>DekuDeals</strong>
        </a>
        </div>
    </footer>
</body>
</html>
''')