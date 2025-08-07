# Ponche Data Update Guide

This guide explains how to update the ponche data from Google Sheets and integrate it into the HTML page.

## Overview

The ponche page uses embedded JSON data directly in the HTML file to avoid server dependencies and CORS issues. When the Google Sheet is updated, follow these steps to refresh the data.

## Step 1: Update Google Sheet

1. **Access the Google Sheet**: `https://docs.google.com/spreadsheets/d/16KsSO3aFWe80XplMn7k4pXi5tag0tUaQbjYFhsjGNO8/edit`
2. **Add new ponches** or modify existing ones
3. **Ensure YouTube links** are in the `youtube_id` column (full URLs like `https://youtu.be/VIDEO_ID?si=...`)
4. **Fill in time data**:
   - `time`: When the ponche occurs (e.g., "2:56")
   - `time_for_attention`: When to start paying attention (e.g., "2:46")
5. **Make sure the sheet is public** (anyone with link can view)

## Step 2: Fetch Updated Data

Run the Python script to fetch the latest data:

```bash
python fetch_data.py
```

This will:
- Download data from the Google Sheet
- Convert it to JSON format
- Save it as `ponche_data.json`
- Show success/error messages

## Step 3: Clean and Filter Data

The script automatically:
- Filters out empty entries (where `song` is empty)
- Preserves all columns from the Google Sheet
- Maintains the exact structure needed for the HTML

## Step 4: Update HTML with New Data

### Option A: Manual Update (Recommended)

1. **Open `ponche_data.json`** and copy the entire content
2. **Open `index.html`** and find the `poncheData` array (around line 300-400)
3. **Replace the existing array** with the new JSON data
4. **Ensure the array ends with**:
   ```javascript
   ].filter(ponche => ponche.song && ponche.song.trim() !== ''); // Filter out empty entries
   ```

### Option B: Automated Update (Advanced)

You could create a script to automatically update the HTML, but manual verification is recommended to ensure data integrity.

## Step 5: Verify the Update

1. **Open `index.html`** in a browser
2. **Click "I'm feeling lucky"** several times to test random selection
3. **Check that**:
   - New ponches appear
   - YouTube thumbnails load correctly
   - Links start at the correct "time for attention"
   - All data fields display properly

## Data Structure

The Google Sheet should have these columns:

| Column | Description | Example |
|--------|-------------|---------|
| `i` | Index number | "0", "1", "2" |
| `song` | Song title | "Modo Van Van" |
| `artist` | Artist name | "Formell y los Van Van" |
| `type` | Type (usually "Ponche") | "Ponche" |
| `ponche_type` | Ponche measure type | "4th_measure", "2nd_measure" |
| `time` | When ponche occurs | "2:56" |
| `time_for_attention` | When to start paying attention | "2:46" |
| `pre_musicality_measure_length` | Pre-musicality info | "8", "4" |
| `size_prominence` | Size/prominence | "Large", "Medium", "Small" |
| `hint for cantante` | Hints for the cantante | "Se Prend Dio!' is sung on the 2nd bar" |
| `youtube_id` | Full YouTube URL | "https://youtu.be/JtX9Tw9vkJA?si=..." |

## Important Notes

### YouTube URLs
- **Use full URLs**: `https://youtu.be/VIDEO_ID?si=...` or `https://youtube.com/watch?v=VIDEO_ID&si=...`
- **Don't use just video IDs**: The system extracts IDs automatically
- **Test URLs**: Make sure they work before adding to the sheet

### Time Format
- **Use MM:SS format**: "2:46", "1:34", "5:01"
- **Be precise**: The system converts to seconds for YouTube timing
- **Time for attention**: Should be slightly before the actual ponche

### Data Quality
- **No empty song titles**: These will be filtered out
- **Consistent formatting**: Keep data clean and consistent
- **Test thoroughly**: Verify each new entry works correctly

## Troubleshooting

### Common Issues

1. **"Video not available"**: YouTube embedding restrictions - this is normal, thumbnails will still work
2. **Wrong timing**: Check that `time_for_attention` is in MM:SS format
3. **Missing data**: Ensure all required columns are filled
4. **Broken links**: Test YouTube URLs before adding to sheet

### Debug Steps

1. **Check console**: Open browser dev tools to see any JavaScript errors
2. **Verify JSON**: Ensure the JSON structure is valid
3. **Test individual entries**: Try specific ponches to isolate issues
4. **Check network**: Ensure YouTube thumbnails are loading

## File Structure

```
im-feeling-ponche/
├── index.html          # Main webpage with embedded data
├── style.css           # Styling
├── fetch_data.py       # Script to fetch from Google Sheets
├── ponche_data.json    # Temporary JSON file (can be deleted after update)
└── prompt_update_data.md # This guide
```

## Future Improvements

Consider these enhancements:
- **Automated updates**: Script to automatically update HTML
- **Data validation**: Check for missing or invalid data
- **Backup system**: Version control for data changes
- **Admin interface**: Web-based data management

---

**Last Updated**: [Current Date]
**Data Source**: Google Sheets - Ponche Database
**Maintainer**: [Your Name/Contact]
