# 🎵 I'm Feeling Ponche - Cuban Music Ponche Database

A beautiful, interactive webpage that randomly displays Cuban music ponches with YouTube integration. Perfect for learning and practicing Cuban dance timing!

## 🌟 Features

- **🎲 Random Ponche Selection** - Click "I'm feeling lucky" to discover new ponches
- **🎬 YouTube Integration** - Direct links to ponche moments with precise timing
- **📱 Responsive Design** - Works perfectly on desktop, tablet, and mobile
- **🎨 Beautiful UI** - Clean, modern design with Pixelify Sans font
- **📊 Detailed Information** - Complete ponche data including timing, hints, and context
- **🔄 Easy Updates** - Simple process to add new ponches from Google Sheets

## 🎯 What is a Ponche?

A "ponche" is a musical break or accent in Cuban music (salsa, son, timba) where the music pauses or changes dramatically. It's a crucial moment for dancers to hit their moves! This tool helps you learn to recognize and anticipate these moments.

## 🚀 Live Demo

Visit the live site: **[https://shaunfg.github.io/im-feeling-ponche/](https://shaunfg.github.io/im-feeling-ponche/)**

## 📋 Current Database

- **37 ponches** from major Cuban artists
- **Featured artists**: Formell y los Van Van, Manolito Simonet, Pupy y Los Que Son Son, and more
- **Multiple ponches per song** where applicable
- **Precise timing** - both ponche time and attention time
- **YouTube links** that start at the exact moment

## 🛠️ Technical Details

### Built With
- **HTML5** - Semantic structure
- **CSS3** - Modern styling with custom fonts
- **JavaScript** - Dynamic content and YouTube integration
- **Google Fonts** - Pixelify Sans for the retro aesthetic

### Key Features
- **No server required** - Pure client-side implementation
- **Embedded data** - All ponche data included in HTML
- **YouTube thumbnail system** - Bypasses embedding restrictions
- **Time conversion** - MM:SS format to YouTube seconds
- **Error handling** - Graceful fallbacks for missing data

## 📁 Project Structure

```
im-feeling-ponche/
├── index.html              # Main webpage with embedded data
├── style.css               # Styling and responsive design
├── fetch_data.py           # Script to update from Google Sheets
├── ponche_data.json        # Current ponche database
├── prompt_update_data.md   # Comprehensive update guide
├── README.md               # This file
└── Pixelify_Sans/          # Custom font files
```

## 🔄 Updating the Database

Want to add more ponches? Check out the **[Update Guide](prompt_update_data.md)** for detailed instructions on:

1. Adding new ponches to the Google Sheet
2. Fetching updated data
3. Updating the HTML file
4. Testing and verification

## 🎨 Design Features

- **Pastel yellow background** - Warm, inviting aesthetic
- **Pixelify Sans font** - Retro gaming vibe
- **Card-based layout** - Clean, organized information
- **Hover effects** - Interactive YouTube-style thumbnails
- **Responsive grid** - Adapts to any screen size

## 🎵 Sample Ponches

- **"Modo Van Van"** by Formell y los Van Van (2:46 attention time)
- **"Muevete"** by Manolito Simonet y su Trabuco (1:34 attention time)
- **"Lola, Lola"** by David Calzado y su Charanga Habanera (2:36 attention time)
- **"Llegar a Viejo"** by Pupy y Los Que Son Son (3:00 attention time)

## 🤝 Contributing

This is a personal project, but suggestions are welcome! If you have:

- **New ponches** to add
- **UI/UX improvements** to suggest
- **Bug reports** to share
- **Feature requests** to propose

Feel free to open an issue or reach out!

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- **Cuban music community** - For the inspiration and knowledge
- **Google Sheets** - For easy data management
- **YouTube** - For hosting the music videos
- **Google Fonts** - For the beautiful Pixelify Sans font

---

**Made with ❤️ for the Cuban music and dance community**

*"I'm feeling ponche!" - Because every day should have a good ponche! 🎵💃*