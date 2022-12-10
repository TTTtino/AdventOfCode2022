Imports System.Reflection

Module Module1

    Function CheckNeighbours(y As Integer, x As Integer, input As ArrayList) As Boolean
        Dim currTreeVal As Integer = input.Item(y).Item(x)
        Dim rowHigh As Integer = input.Item(y).Count - 1
        Dim colHigh As Integer = input.Count - 1
        Dim maxHeight As Integer = -1
        For xIndex As Integer = 0 To x - 1
            maxHeight = Math.Max(maxHeight, input.Item(y).Item(xIndex))
        Next
        If maxHeight < currTreeVal Then Return True
        maxHeight = -1
        For xIndex As Integer = x + 1 To rowHigh
            maxHeight = Math.Max(maxHeight, input.Item(y).Item(xIndex))
        Next
        If maxHeight < currTreeVal Then Return True
        maxHeight = -1
        For yIndex As Integer = 0 To y - 1
            maxHeight = Math.Max(maxHeight, input.Item(yIndex).Item(x))
        Next
        If maxHeight < currTreeVal Then Return True
        maxHeight = -1
        For yIndex As Integer = y + 1 To colHigh
            maxHeight = Math.Max(maxHeight, input.Item(yIndex).Item(x))
        Next
        If maxHeight < currTreeVal Then Return True

        Return False
    End Function

    Function ScenicScore(y As Integer, x As Integer, input As ArrayList) As Integer
        Dim currTreeVal As Integer = input.Item(y).Item(x)
        Dim rowHigh = input.Item(0).Count - 1
        Dim colHigh = input.Count - 1
        Dim score
        Dim dirScore = 0
        For i As Integer = x - 1 To 0 Step -1
            If input.Item(y).Item(i) >= currTreeVal Then
                dirScore += 1
                Exit For
            Else
                dirScore += 1
            End If
        Next
        'Console.WriteLine(dirScore.ToString + " Left Score")
        score = dirScore
        dirScore = 0
        For i As Integer = x + 1 To rowHigh
            If input.Item(y).Item(i) >= currTreeVal Then
                dirScore += 1
                Exit For
            Else
                dirScore += 1
            End If
        Next
        score *= dirScore
        'Console.WriteLine(dirScore.ToString + " Right Score")
        dirScore = 0
        For i As Integer = y - 1 To 0 Step -1
            If input.Item(i).Item(x) >= currTreeVal Then
                dirScore += 1
                Exit For
            Else
                dirScore += 1
            End If
        Next
        score *= dirScore
        'Console.WriteLine(dirScore.ToString + " Top Score")
        dirScore = 0
        For i As Integer = y + 1 To colHigh
            If input.Item(i).Item(x) >= currTreeVal Then
                dirScore += 1
                Exit For
            Else
                dirScore += 1
            End If
        Next
        'Console.WriteLine(dirScore.ToString + " Bottom Score")
        score *= dirScore
        Return score
    End Function

    Sub Main()
        Dim file As String = IO.Path.Combine(My.Application.Info.DirectoryPath, "input.txt")
        Dim trees As New ArrayList
        FileOpen(1, file, OpenMode.Input)
        Do While Not EOF(1)
            Dim line As String = LineInput(1).Trim()
            Dim treeRow As New ArrayList
            For i As Integer = 0 To line.Length - 1
                Dim int As Integer = Convert.ToInt32(line.Substring(i, 1))
                treeRow.Add(int)
            Next
            trees.Add(treeRow)
        Loop

        FileClose(1)
        Dim count = 0
        Dim maxScenicScore = -1
        Dim rowLen = trees.Item(0).Count
        Dim colLen = trees.Count
        For y As Integer = 1 To trees.Count - 2
            Dim treeRow As ArrayList = trees.Item(y)
            For x As Integer = 1 To treeRow.Count - 2
                Console.Write("{0}Current: {1}/{2}", vbCr, (y - 1) * rowLen + x + 1, rowLen * colLen)
                If CheckNeighbours(y, x, trees) Then count += 1
                maxScenicScore = Math.Max(maxScenicScore, ScenicScore(y, x, trees))
            Next
        Next
        Console.WriteLine()
        Console.WriteLine((count + trees.Count * 2 + trees.Item(0).Count * 2 - 4).ToString + ", " + maxScenicScore.ToString)
        Console.ReadLine()
    End Sub

End Module
