FOLDERS = {
    "HTML":       [
                   ".html5", ".html", ".htm", ".xhtml",
    ],
    "DIFs":       [
                   ".xml", ".json", ".csv", ".xls", ".xlsx", ".dif", ".yaml"
    ],
    "Images":     [
                   ".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg",
                   ".svg", ".heif", ".psd", "webp",
    ],
    "Videos":     [
                   ".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob",
                   ".mng", ".qt", ".mpg", ".mpeg", ".3gp",
    ],
    "Documents":  [
                   ".oxps", ".epub", ".pages", ".docx", ".doc", ".fdf", ".ods",
                   ".odt", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox",
                   ".rvg", ".rtf", ".rtfd", ".wpd",  ".ppt", ".pptx", ".pdf",
                   ".md"
    ],
    "Archives":   [
                   ".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z",
                   ".dmg", ".rar", ".xar", ".zip",
    ],
    "Audios":     [
                   ".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p",
                   ".mp3", ".msv", "ogg", "oga", ".raw", ".vox", ".wav",
                   ".wma",
    ],
    "Plaintexts": [
                   ".txt", ".in", ".out",
    ],
    "Programs":   [
                   ".exe", ".msi",
    ],
    "Python":     [
                   ".py", ".pyc", ".pynnb"
    ],
    "Ruby":       [
                   ".rb"    
    ],
    "Shells":     [
                   ".sh",
    ],
    "Torrents":   [
                   ".torrent",
    ],
}

def get_file_formats():
    mapped_file_extension = {}
    
    for directory, file_formats in FOLDERS.items():
        for file_format in file_formats:
            mapped_file_extension[file_format] = directory
    
    return mapped_file_extension
