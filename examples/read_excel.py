import xlrd

workbook = xlrd.open_workbook('../Metadata.xlsx')

allSheet = workbook.sheet_by_index(0)

for i in range(allSheet.nrows):
    print(allSheet.row_values(i))


class Metadata:
    def __init__(self, na, file_name, source, title, creator, dateCreated, coverageSpatial, menuItem, subFolder,
                 subjects, keywords, work_areas, languages, license):
        self.na = na
        self.fileName = file_name
        self.source = source
        self.title = title
        self.creator = creator
        self.dateCreated = dateCreated
        self.coverageSpatial = coverageSpatial
        self.menuItem = menuItem
        self.subFolder = subFolder
        self.subjects = subjects
        self.keywords = keywords
        self.workAreas = work_areas
        self.languages = languages
        self.license = license