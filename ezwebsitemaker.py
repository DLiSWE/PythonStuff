'''Create base tag object. Will have both opening and closing brackets that most
html synax use. Set init to default. Stringify it. Print it
'''
class Tag(object):

    def __init__(self, name, contents):
        self.start_tag = '<{}>'.format(name)
        self.end_tag = '</{}>'.format(name)
        self.contents = contents


    def __str__(self):
        return "{0.start_tag}{0.contents}{0.end_tag}".format(self)

    def display(self, file=None):
        print(self, file=file)

#Create tag object for image source. Single <> with content inside. No closing bracket
class ImgSourcTag(object):

    def __init__(self, contents):
        self.contents = '<{}>'.format(contents)

    def __str__(self):
        return "{0.contents}".format(self)

    def display(self, file=None):
        print(self, file=file)

class DocType(Tag):

    def __init__(self):
        super().__init__('!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" http://www.w3.org/TR/html4/strict.dtd', '')
        self.end_tag = ''   # DOCTYPE doesn't have an end tag

#Create head class. Allow additional tags within head tag & make function to display and append results
class Head(Tag):

    def __init__(self):
        super().__init__('head', '')
        self._head_contents = []

    def add_htag(self, name, contents):
        new_htag = Tag(name, contents)
        self._head_contents.append(new_htag)

    def display(self, file=None):
        for tag in self._head_contents:
            self.contents += str(tag)

        super().display(file=file)

#Create Body class. Allow additional tags within body tag & make function to display and append results
class Body(Tag, ImgSourcTag):

    def __init__(self):
        super().__init__('body style="background-color: grey;"', 'Body Starts Here') #TODO: build body contents
        self._body_contents = []

    def add_tag(self, name, contents):
        new_tag = Tag(name, contents)
        self._body_contents.append(new_tag)

    def add_istag(self, contents):
        new_istag = ImgSourcTag(contents)
        self._body_contents.append(new_istag)

    def display(self, file=None):
        for tag in self._body_contents:
            self.contents += str(tag)

        super().display(file=file)

#create HTML document object
class HtmlDoc(object):

    def __init__(self):
        self._doc_type = DocType()
        self._head = Head()
        self._body = Body()

    def add_tag(self, name, contents):
        self._body.add_tag(name, contents)

    def add_istag(self, contents):
        self._body.add_istag(contents)

    def add_htag(self, name, contents):
        self._head.add_htag(name,contents)

    def display(self, file=None):
        self._doc_type.display(file=file)
        print('<html>', file=file)
        self._head.display(file=file)
        self._body.display(file=file)
        print('</html>', file=file)

#Main function. Add tags here.
'''use add_istag for single bracket syntax without closing bracket like <img src>.
use add_tag for opening and closing bracking
first parameter is content within first bracket and second parameter is what you want inside the <>...</> syntax
For styling, include the style within the first parameter'''
if __name__ == '__main__':
    my_page = HtmlDoc()
    my_page.add_htag('title', 'Page Name')
    my_page.add_tag('h1 style="background-color:powderblue; text-align:center;"', 'Main heading')
    my_page.add_tag('h2 style="background-color:skyblue; text-align:center;"', 'sub-heading')
    my_page.add_tag('style', '.myDiv { border: 5px outset red; background-color: lightblue; text-align: center; }')
    my_page.add_tag('div class="myDiv"', '<h2>Need to create new class for divs</h2><p>forgot about this</p>')
    my_page.add_istag('img src="testimg.jpg" alt="image description"')
    my_page.add_tag('p style="background-color:blue;"', 'paragraph blah blah blah')
    with open('test.html', 'w') as test_doc:
        my_page.display(file=test_doc)
