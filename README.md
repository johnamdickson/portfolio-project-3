
# <img src="views/README-files/icon.png"  width="50" height="50"> Weather: Past or Forecast?

Weather: Past or Forecast is a command line application that allows the user to check past weather or get a weather forecast directly from the terminal.

This application is showcasing Python coding for Project Portfolio 3 and can be accessed by following this [link.] **ADD LINK

![Responsive Mockup Screenshot](views/README-files/am-i-responsive.png)

## Contents
<a name="contents"></a>

- [UX](#ux)
  - [Strategy](#strategy)
    - [User Stories](#user-stories)
  - [Scope](#scope)
    - [Essential Content](#essential-content)
    - [Optional Content](#optional-content)
  - [Structure](#structure)
  - [Skeleton](#structure)
    - [Wireframes](#wireframes)
  - [Surface(Design)](#surface-design)
    - [Colour Scheme](#colour-scheme)
    - [Imagery](#imagery)
    - [Favicon](#favicon)
- [Features](#features)
  - [Existing Features](#existing-features)
  - [Features Left to Implement](#features-left-to-implement)
- [Technologies Used](#technologies-used)
  - [Languages Used](#languages-used)
  - [Frameworks, Libraries & Programs Used](#frameworks-libraries--programs-used)
- [Testing](#testing)
  - [Development Testing](#development-testing)
  - [Testing User Stories](#testing-user-stories)
     - [User Goals](#user-goals)
     - [Site Administrator Goals](#site-administrator-goals)
  - [Responsiveness Testing](#responsiveness-testing)
    - [Physical Device](#physical-device)
    - [Simulated Devices](#simulated-devices)
  - [Browser Compatability](#browser-compatability)
  - [Validator Testing](#validator-testing)
  - [Bugs / Issues](#bugs--issues)
  - [Unresolved Bugs / Issues](#unresolved-bugs-or-issues)
- [Deployment](#deployment)
  - [Git Hub Pages](#github-pages)
  - [Forking the GitHub Repository](#forking-the-github-repository)
  - [Making a Local Clone](#making-a-local-clone)
- [Credits](#credits)
  - [Content](#content)
  - [Media](#media)




## UX
### Strategy
The objective of the site is to allow users to review past weather for a location in Ireland or obtain a weather forecast for a geographic location using coordinates.
#### User Stories
- User Goals:
  - To access the historical weather for a selected date at Dublin airport.
  - To access a 3 day weather forecast for a given location.
  - To be able to leave feedback on the app.
<br><br>
- Site Administrator Goals:
  - To give users the options to access historical weather, weather forecasts and have the option to create, read, update and delete feedback.
  - To create an application using Python with clean, resuable and commented code, utilising atomic functionality and OOP where appropriate.
  - To handle any potential errors appropriately.
  - To maintain secrecy of API key for weather data provider.

### Scope
#### Essential Content
 - The app will allow users to enter a date and receive the weather for that given day.
 - The app will allow users to enter latitude and longitude coordinates to obtain a weather forecast for that location. 
#### Optional Content
- A feedback option where users can leave their feedback on the app.
### Structure
The structure of the app was defined and mapped out on a [flow chart](views/README-files/flowchart.png). This helped define the required interactions to develop a usuable product.
### Skeleton
#### Wireframes
- The project wireframe can be found [here.](views/README-files/project-portfolio-three-wireframes.pdf)
### Surface (Design)
#### Colour Scheme
- The Termcolor library was used, providing *"ANSI color formatting for output in terminal"*.
- The availalble colours are limited however the following colour schemes were used for specific terminal outputs throughout the program:
  - **Errors**: errors (invalid entries, exceptions etc.) are formatted with bold white writing on a red background.<br><br>![Error Message](views/README-files/error-message-formatting.png)
  - **Information**: information that the user should know before taking an action formatted as bold green.<br><br> ![Information Message](views/README-files/information-message-formatting.png)
  - **Data**: pertinent data points either sourced/calculated from Google Sheets or Open Weather API are formatted as bold blue.<br><br> ![Data Message](views/README-files/data-message-formatting.png)
  - **Feedback**: a message to request the user does not leave the feedback message empty in bold magenta. Although this could be deemed an app error, I felt that the white on red would be too forceful to request feedback is entered. <br><br>![Feedback Message](views/README-files/feedback-message-formatting.png)
- There are a series of screens using text art to depict titles or loading information. Different colours were selected for each one to differentiate them from the others.
  - **Title**: Displayed when the program first runs.![Title Screen](views/README-files/title-screen.png)
  - **Loading**: Displayed when the program is laoding data that may take time to load.<br><br>
  ![Loading Screen](views/README-files/loading-screen.gif)
  - **Forecast Days**: Displayed when the program is about to display the weather for a given forecast day.![Day One](views/README-files/forecast-one.png) ![Day Two](views/README-files/forecast-two.png) ![Day Three](views/README-files/forecast-three.png)
#### Imagery
- The background image was sourced from [Pexels](https://www.pexels.com/) and was selected for exhibiting a number of different weather types in one image.
![Background Image](views/README-files/background-picture.webp)
- Two weather icon images were sourced from [Favicon.io](https://favicon.io/) to bookend the main title.<br><br>
<img src="views/images/title-icon-bolt.png"  width="200" height="200"> <img src="views/images/title-icon-sun.png"  width="200" height="200">

#### Favicon
- The Favicon logo is the lightning bolt image described above.
#### Typography
- The title font was sourced from Google Fonts and is called Merriweather. This was selected purely on the presence of weather in the name and was seen as a good link back to the purpose of the app.<br>
<a href="#contents">BACK TO CONTENTS 🔼</a>

## Features 

### Existing Features

- __Starting Options__ <br><br>
![Game-Information](assets/README-files/game-information.png)

  - **ADD<br><br>
- __Past Weather__ <br><br>
![Game-Instructions](/assets/README-files/game-instructions.jpg) 

  - **ADD<br><br>
- __Weather Forecast__ <br><br>
![Game Area](/assets/README-files/game-area-flip-two-cards.gif)

    - **ADD
- __Feedback__ <br><br>
![Player-Information](/assets/README-files/player-info.gif)

  - **ADD<br><br>

### Features Left to Implement
- **ADD

<a href="#contents">BACK TO CONTENTS 🔼</a>

## Technologies Used

### Languages Used
- **Python**: used extensively during project.
- **Markdown**: Used exclusively for README.
- **HTML5**: minor use when adding additional elements to the web page.
- **CSS3**: minor use when applying styling to app view.<br>

### Frameworks, Libraries & Programs Used
- **gspread**: used to complete CRUD actions on Google Sheets.
- **Credentials**: imported from google.oauth.serivice_account to enable access to Google Sheets.
- **termcolor**: used to apply foreground and background colors to terminal text.
- **datetime**: from the standard library, used to perform operations on date and time objects and strings.
- **numpy**: used to create a range of floats due to python range only returning a range of integers.
- **itertools**: from standard library used to iterate over list for loading animation.
- **pyowm**: library with classes used to manage Open Weather API calls.
- **time**: from the standard library used to access sleep method for pauses during pertinent points of relaying information to the user.
- **os**: from the standard library used to access system method to clear terminal screen at appropriate points whilst the program is running.
- **tabulate**: used to create a table of contents in the feedback and weather forecast sections of the app.
- **threading**: used to enable multithreading operations used for loading screens.

<br><a href="#contents">BACK TO CONTENTS 🔼</a>
## Testing 
### Development Testing

- __Starting Options__
  - The app started successfully using the Run Program button with the title ANSI graphic title text being presented followed by the main menu.
  - Entering 1 or 2 directed the user to the correct section of the app.  <br><br>
- __Past Weather__
  - The past weather date entry page loaded successfully giving the user the information required and the correct prompt to enter the selected date.
  ![past-weather](views/README-files/past-weather-date-entry.png)
  - When a valid date is entered, the screen clears and a series of statements are printed out in readable language with the data obtained or calculated from the Google Sheet formatted in bold blue. ![past-weather](views/README-files/past-weather.gif)
  - After a delay, a user options menu is presented to return to the main menu, look for past weather, run a weather forecast for chosen location or leave feedback. The user options menu testing is detailed later on in this section. 
  - Various errors were purposefully entered into the terminal to check the app response as detailed below:
    - *Incorrect date format*: a variety of non-date related strings and characters were entered into the terminal with the expected response detailed below: ![date-validation-error](views/README-files/date-validation-message.png) The message remained on screen for 3 seconds at which point the Past Weather date entry page reappears to allow user to try and enter a date again.
    - *Date out of range*: a date outwith the data range contained in the Google Sheet was entered. The loading screen was presented allowing the program to check the date given lies within the archive data range. As expected, the program presented the user with the following error message:![date-out-of-range-error](views/README-files/date-out-of-range-message.png) As in the message above, it remained on screen for 3 seconds before returning to the Past Weather date entry page.
- __Weather Forecast__
  - The forecast weather coordinate entry page loaded successfully giving the user the information required and the correct prompt to enter the required latitude and longitude. ![forecast-weather](views/README-files/weather-forecast-coord-entry.png)
  - On receipt of valid coordinates, the app presents todays forecast. This consists of a title screen followed by feedback on location and date of forecast. This is then followed by weather icon with conditions underneath before a series of readable language statements is presented with the data obtained or calculated from the Open Weather API formatted in bold blue. ![weather-forecast](views/README-files/weather-forecast-today.gif)
  - After a delay a prompt to hit enter to see the next days forecast is presented to the user. Hitting enter runs tomorrows forecast which is identical to the process above and then hitting enter at end of tomorrows forecast returns the day after tomorrows forecast.
  - At the end of the day after tomorrows forecast, the user options menu is presented with the same options as described in the Past Weather development testing section with an additional option to see a 5 day summary. This will be described in more detail in the User Options section below.
  - Various errors were purposefully entered into the terminal or manaully created to check the app response as detailed below:
    - *Single entry*: a single entry was made in the terminal which correctly resulted in the error message below: ![single-entry-error](views/README-files/one-entry-weather-forecast.png) The message remained on screen for 3 seconds at which point the Weather Forecast coordinate entry page reappears to allow user to try and enter coordinates again.
    - *Too many entries*: three numbers were entered which resulted in the error message below: ![too-many-entries-error](views/README-files/too-many-entries-message.png) The message persisted for 3 seconds before returning to the coordinate entry page.
    - *Latitude out of range*: a latitude was entered which was not within the acceptable range of -90 to 90 resulting in the error message below: ![incorrect latitude-error](views/README-files/incorrect-latitude-message.png) The message persisted for 3 seconds before returning to the coordinate entry page.
    - *Longitude out of range*: a longitude was entered which was not within the acceptable range of -180 to 180 resulting in the error message below: ![incorrect longitude-error](views/README-files/incorrect-longitude-message.png) The message persisted for 3 seconds before returning to the coordinate entry page.
    - *API errors*: a single digit was deleted from the API key config var in Heroku to simulate an error returned from the API which generated the message below: ![api-error](views/README-files/invalid-api-message.png) The message persisted for 3 seconds however in this instance, the user menu was made available as the user may want to navigate away from the Weather Forecast, given that the error came from the API so may be a time bound issue on the providers side.

- __Feedback__
  - **ADD.<br><br>
- __User Options__
  - **ADD.<br><br>

### Testing User Stories
**ADD
#### User Goals
- **ADD**
  - **ADD

#### Site Administrator Goals
  - **ADD.**
    - **ADD

### Validator Testing 

- HTML
  - No errors or warnings were returned for the page when passing through the official W3C HTML validator:
    ![HTML Validator Results](views/README-files/w3-html-validator-results.png)<br><br> 
    
- CSS
  - No errors were returned for the page when passing through the official W3C CSS validator:
    ![CSS Validator Results](/views/README-files/w3-css-validator-results.png) 
    There were two warnings returned, both linked to code that existed from the CI template.<br><br>

- Python
  - **ADD.
  ![JSHint Validator Results](/assets/README-files/jshint.png)<br><br> 

- Accessibility
  - Accessibility of the page was checked using the lighthouse tool in devtools. The results were satisfactory as shown below. **ADD
     - Desktop results:
     ![Lighthouse Results](views/README-files/lighthouse-results.png) <br><br>
  - The colour contrasts **ADD.<br><br>
  
  <table  width = 100% cellspacing="0" cellpadding="0">
  <tr>
  <td><img src="assets/README-files/biscay-confetti-contrast.png" ></td>
  <td> <img src="assets/README-files/biscay-powder-blue-contrast.png"></td>
  </tr>
  </table>

 
<a href="#contents">BACK TO CONTENTS 🔼</a>
### Bugs / Issues
**ADD
<table  width = 100% cellspacing="0" cellpadding="0">
   <tr>
   <th>Issue/Bug</th>
   <th>Solution</th>
   </tr>
   <tr>
   <td>**ADD</td>
   <td>**ADD</td>
   </tr>
   <tr>
   <td>**ADD</td>
   <td>**ADD</td>
   </tr>
   <tr>
   <td>**ADD</td>
   <td>**ADD</td>
   </tr>
   <tr>
   <td>**ADD</td>
   <td>**ADD</td>
   </tr>
   <tr>
   <td>**ADD</td>
   <td>**ADD</td>
   </tr>
   <tr>
   <td>**ADD</td>
   <td>**ADD</td>
   </tr>
  </table>

### Unresolved Bugs or Issues
- **ADD. <br><br>
<a href="#contents">BACK TO CONTENTS 🔼</a>

## Deployment

### GitHub Pages
The site was deployed to GitHub pages. The steps to deploy are as follows: 
1. Log in to GitHub and locate the [GitHub Repository.](https://github.com/)
2. Under the repository name, click ⚙ Settings. If you cannot see the "Settings" tab, select the  dropdown menu, then click Settings.
3. In the "Code and automation" section of the sidebar, click  Pages
4. Under "Build and deployment", under "Branch", use the None or Branch dropdown menu and select a publishing source.
5. Once the master branch has been selected, the page will be automatically refreshed with a detailed ribbon display to indicate the successful deployment. 

The live link can be found [here.](https://johnamdickson.github.io/Portfolio-Project-2/index.html)

### Forking the GitHub Repository

By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps:

1. Log in to GitHub and locate the [GitHub Repository.](https://github.com/johnamdickson/Portfolio-Project-2)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. You should now have a copy of the original repository in your GitHub account.

### Making a Local Clone

1. Log in to GitHub and locate the [GitHub Repository.](https://github.com/johnamdickson/Portfolio-Project-2)
2. Under the repository name, click "Clone or download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, and then paste the URL you copied in Step 3.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
```

7. Press Enter. Your local clone will be created.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
> Cloning into `CI-Clone`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```

Click [Here](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop) to retrieve pictures for some of the buttons and more detailed explanations of the above process.<br><br>
<a href="#contents">BACK TO CONTENTS 🔼</a>
## Credits 
### Content 
NOTE: Specific links are included within the HTML, CSS or Javascript files. The list below summarises content credits in general.
- Stack Overflow, W3 Docs, MDN Web Docs and other online resources were a massive help for HTML, CSS or JS code that enabled some of the functionality I was looking for.
- Beafort scale used to describe weather from given wind speed. Source in [wikipedia.](https://en.wikipedia.org/wiki/Beaufort_scale)
- Cardinal and ordinal wind directions taken from [Windy](https://windy.app/blog/what-is-wind-direction.html).
- **ADD
### Media
- Merriweather font was sourced from Google Fonts.
- All gifs were generated on [ezif.com.](https://ezgif.com/video-to-gif)
<br><br>
<a href="#contents">BACK TO CONTENTS 🔼</a>
