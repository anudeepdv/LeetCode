class SQL:

    def __init__(self, names: List[str], columns: List[int]):
        self.tableToRow={}
        self.tableTodata={}
        for i in names:
            self.tableToRow[i]=1
            self.tableTodata[i]={}    

    def insertRow(self, name: str, row: List[str]) -> None:
        curRowId = self.tableToRow[name]
        self.tableTodata[name][curRowId]=row
        self.tableToRow[name]=self.tableToRow[name]+1

    def deleteRow(self, name: str, rowId: int) -> None:
        del self.tableTodata[name][rowId]

    def selectCell(self, name: str, rowId: int, columnId: int) -> str:
        # print(self.tableTodata[name])
        # print(rowId,columnId)
        return self.tableTodata[name][rowId][columnId-1]
        


# Your SQL object will be instantiated and called as such:
# obj = SQL(names, columns)
# obj.insertRow(name,row)
# obj.deleteRow(name,rowId)
# param_3 = obj.selectCell(name,rowId,columnId)