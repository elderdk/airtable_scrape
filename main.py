import library.parse_site as parse_site
# import VSCode.Upwork.Airtable.library.parse_site as parse_site


if __name__ == "__main__":
    
    parse_site.main(
        url = "https://airtable.com/shrtGl2KvVkV4Bnvu/tblwG5Fvuz8B2ZJ2U?backgroundColor=red&viewControls=on",
        fname = 'Airtable_scrape.xlsx',
        wait_time = 0,
        sheet_name = 'Sheet1',
        headless = True
    )


#make proper folder structure
#check if the entry already exists and skip if so