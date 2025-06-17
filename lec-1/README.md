````markdown
# 🚀 Lecture 1: Introduction to HTML

## 📖 What is HTML?

HTML (**HyperText Markup Language**) is the standard language used to **create and structure web pages**. It tells your browser *what content to display and how to display it*.

Think of HTML as the **skeleton** of a webpage. It works alongside:

- **CSS** – for styling (colors, fonts, layouts)
- **JavaScript** – for functionality and interactions

---

## 🧱 Basic Structure of an HTML Document

```html
<!DOCTYPE html>
<html>
  <head>
    <title>My Website</title>
  </head>
  <body>
    <!-- Your content goes here -->
  </body>
</html>


### 🔍 What each part does:

* `<!DOCTYPE html>` – Declares HTML5 version.
* `<html>` – Root element of the page.
* `<head>` – Metadata (title, charset, CSS links, etc.).
* `<body>` – All visible content goes here.

---

## ✍️ Text Elements

| Tag                 | Description                    |
| ------------------- | ------------------------------ |
| `<h1>` to `<h6>`    | Headings (largest to smallest) |
| `<p>`               | Paragraph                      |
| `<br>`              | Line break                     |
| `<hr>`              | Horizontal rule                |
| `<b>` or `<strong>` | Bold text                      |
| `<i>` or `<em>`     | Italic text                    |
| `<u>`               | Underlined text                |

---

## 📋 Lists

### ✅ Ordered List:

```html
<ol>
  <li>First</li>
  <li>Second</li>
</ol>
```

### 🔹 Unordered List:

```html
<ul>
  <li>Item 1</li>
  <li>Item 2</li>
</ul>
```

---

## 🔗 Hyperlinks

```html
<a href="https://www.google.com" target="_blank">Open Google</a>
```

* `target="_blank"` opens the link in a new tab.
* You can also use `mailto:` or internal page links.

---

## 🖼️ Images

```html
<img src="image.jpg" alt="Image description">
```

* `src` = source of the image (URL or file)
* `alt` = alternative text shown if image doesn’t load

---

## 📊 Tables

```html
<table border="1">
  <tr>
    <th>Name</th>
    <th>Age</th>
    <th>Subject</th>
  </tr>
  <tr>
    <td>Aryan</td>
    <td>18</td>
    <td>Math</td>
  </tr>
</table>
```

You can also use:

* `colspan` to merge columns
* `rowspan` to merge rows

---

## 🧪 Mini Project Assignment: Create Your First Web Page

✅ **Instructions:**
Create a single `.html` file using only HTML. Include all tasks below in that one file.

---

### ✏️ **Q1: Basic Web Page**

* Add a title: **"My First Web Page"**
* Use `<h1>` and `<h2>` for headings
* Add **2 paragraphs** about yourself
* Insert an `<hr>` between paragraphs

---

### ✏️ **Q2: Text Formatting**

* Write a sentence using:

  * **Bold** using `<b>` or `<strong>`
  * *Italic* using `<i>` or `<em>`
  * *Underline* using `<u>`
* Add a `<br>` between two lines

---

### ✏️ **Q3: Lists**

* Create:

  * An **ordered list** of 5 favorite websites
  * An **unordered list** of 5 favorite foods

---

### ✏️ **Q4: Hyperlink & Image**

* Add a hyperlink to your favorite website (open in new tab)
* Add an image (`<img>`) from the web or local folder
* Use the `alt` attribute to describe the image

---

### ✏️ **Q5: Create a Table**

* Make a table with:

  * 3 rows (students)
  * 4 columns (Name, Age, Subject, Grade)
* Use:

  * `colspan` in one row
  * `rowspan` in another

````
