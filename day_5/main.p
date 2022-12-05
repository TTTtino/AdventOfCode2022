{$mode objfpc} // directive to be used for defining classes
{%m +}

uses
  SysUtils,
  StrUtils;

type
  TStack = class
    private
      FData: array of variant;
      FCount: integer;
    public
      constructor Create;
      constructor Create(initData: array of variant);
      procedure Push(AValue: variant);
      function Pop: variant;
      function Peek: variant;
      function IsEmpty: boolean;
      procedure Debug;
      property Count: integer read FCount;
  end;


constructor TStack.Create(initData: array of variant);
var
   i: integer;
begin
  FCount := Length(initData);
  SetLength(FData, FCount);
  for i := 0  to FCount-1 do
     begin
        FData[i] := initData[i];
     end;
end;

constructor TStack.Create;
begin
  FCount := 0;
  SetLength(FData, 0);
end;

procedure TStack.Push(AValue: variant);
begin
  Inc(FCount);
  SetLength(FData, FCount);
  FData[FCount - 1] := AValue;
end;

function TStack.Pop: variant;
begin
  if FCount > 0 then
  begin
    Result := FData[FCount - 1];
    Dec(FCount);
    SetLength(FData, FCount);
  end

end;

function TStack.Peek: variant;
begin
  if FCount > 0 then
    Result := FData[FCount - 1]
end;

function TStack.IsEmpty: boolean;
begin
  Result := FCount = 0;
end;

procedure TStack.Debug;
var
  i: integer;
begin
  for i := 0 to High(FData) do
  begin
     WriteLn(FData[i]);
  end;
end;


type
  TStringArray = array of string;
  TStackArray = array of TStack;

type
  TParsedOutput = record
    Stacks: TStackArray;
    Procs: array of array of integer;
  end;

function SplitString(input: string): TStringArray;
var
  words: TStringArray;
  i, j, wordStart: Integer;
begin
  // Set the length of the words array
  SetLength(words, WordCount(input, [' ']));

  // Split the input string into individual words
  wordStart := 1;
  for i := 0 to High(words) do
  begin
    j := wordStart;
    while (j <= Length(input)) and (input[j] <> ' ') do
      Inc(j);
    words[i] := Copy(input, wordStart, j - wordStart);
    wordStart := j + 1;
  end;

  // Return the resulting array of words
  Result := words;
end;


function ReadLinesFromFile(AFileName: string): TStringArray;
var
  MyFile: TextFile; // The file that we will read from
  MyArray: TStringArray; // The array that will hold the lines from the file
  S: string; // A string variable to hold each line as we read it from the file
begin
  // Open the file for reading
  AssignFile(MyFile, AFileName);
  Reset(MyFile);

  // Set the length of the array to 0
  SetLength(MyArray, 0);

  // Read each line from the file and add it to the array
  while not EOF(MyFile) do
  begin
    ReadLn(MyFile, S);
    SetLength(MyArray, Length(MyArray)+1);
    MyArray[Length(MyArray) - 1] := S;
  end;

  // Close the file and return the array
  CloseFile(MyFile);
  Result := MyArray;
end;

function ParseStacksFromStringArray(StringArr: TStringArray): TParsedOutput;
var
  StringStacks: array of string;
  ProcStrings: array of string;
  Stacks: TStackArray;
  Procs: array of array of integer;
  CurrentProc: array of integer;
  NumOfContainers: integer;
  str: string;
  IsStacks: boolean;
  ProcTokens: array of string;
  i, j: integer;
begin
  Stacks := [];
  Procs := [];
  StringStacks := [];
  ProcStrings := [];
  IsStacks := true;
(* Turn the string into array of stack string and array of procedure strings *)
  for i := 0 to High(StringArr) do
    begin
      str := StringArr[i];
      if (' 1' <> Copy(str, 1, 2)) and (IsStacks) then
        begin
        SetLength(StringStacks, Length(StringStacks)+1);
        StringStacks[High(StringStacks)] := str;
        end
      else
        begin
        if (' 1'=Copy(str, 1, 2)) then
          begin
            NumOfContainers := StrToInt(str[Length(str)-1]);
            IsStacks := false;
          end
        else
          begin
            SetLength(ProcStrings, Length(ProcStrings)+1);
            ProcStrings[High(ProcStrings)] := str;
          end
        end
    end;
(* Parse the string stacks *)
  for j := 0 to(NumOfContainers-1) do
    begin
      SetLength(Stacks, Length(Stacks)+1);
      Stacks[High(Stacks)] := TStack.Create;
    end;
  for i := 0 to High(StringStacks) do
  begin
    str := StringStacks[High(StringStacks) - i];
    for j := 0 to(NumOfContainers-1) do
    begin
      if (str[2 + j * 4] <> ' ') then
        Stacks[j].Push(str[2 + j * 4])
    end;
  end;
(* Parse the string procedures  *)

  for i := 0 to High(ProcStrings) do
  begin
    str := ProcStrings[i];
    ProcTokens := SplitString(str);
    SetLength(CurrentProc, 3);
(* for j := 0 to High(ProcTokens) do
    begin
      WriteLn(ProcTokens[j]);
    end; *)
    if Length(ProcTokens) >= 6 then
      begin
      SetLength(Procs, Length(Procs)+1);
      Procs[High(Procs)] := [StrToInt(ProcTokens[1]), StrToInt(ProcTokens[3]), StrToInt(ProcTokens[5])];
      end
  end;
(*   for i := 0 to High(Procs) do
  begin
    for j := 0 to High(Procs[i]) do
    begin
      WriteLn(Procs[i][j]);
    end;
  end; *)
  Result.Stacks := Stacks;
  Result.Procs := Procs;
end;

function MoveBetweenStacksPart1(NumToMove: integer; FromStackI: integer; ToStackI: integer; Stacks: TStackArray): TStackArray;
var
  FromStack: TStack;
  ToStack: TStack;
  PoppedVal: string;
  i: integer;
begin
  FromStack := Stacks[FromStackI];
  ToStack := Stacks[ToStackI];

  for i := 0 to NumToMove-1 do
    begin
      PoppedVal := FromStack.Pop;
      ToStack.Push(PoppedVal);
    end;
  Stacks[FromStackI] := FromStack;
  Stacks[ToStackI] := ToStack;
  Result := Stacks;
end;

function MoveBetweenStacksPart2(NumToMove: integer; FromStackI: integer; ToStackI: integer; Stacks: TStackArray): TStackArray;
var
  FromStack: TStack;
  ToStack: TStack;  
  TempStack: TStack;
  PoppedVal: string;
  i: integer;
begin
  TempStack := TStack.Create;
  FromStack := Stacks[FromStackI];
  ToStack := Stacks[ToStackI];

  for i := 0 to NumToMove-1 do
    begin
      PoppedVal := FromStack.Pop;
      TempStack.Push(PoppedVal);
    end;
  while (not TempStack.IsEmpty) do
    begin
      ToStack.Push(TempStack.Pop);
    end;
  Stacks[FromStackI] := FromStack;
  Stacks[ToStackI] := ToStack;
  Result := Stacks;
end;

var
  InputArr: TStringArray;
  Stacks: TStackArray;
  ParsedOutput: TParsedOutput;
  procedures: array of array of integer;
  MyStack: TStack;
  Output: string;
  i,j : integer;
  t: string;
begin
  InputArr := [];
  Stacks := [];
  InputArr := ReadLinesFromFile('input.txt');
  t := '';
  ParsedOutput := ParseStacksFromStringArray(InputArr);
  Stacks := ParsedOutput.Stacks;
  for i := 0 to High(ParsedOutput.Procs) do
    begin
      Stacks := MoveBetweenStacksPart2(ParsedOutput.Procs[i][0], ParsedOutput.Procs[i][1]-1, ParsedOutput.Procs[i][2]-1, Stacks);
    end;
  Output := '';
  for i := 0 to High(ParsedOutput.Stacks) do
    begin
      Output := Output + ParsedOutput.Stacks[i].Pop
    end; 
  WriteLn(Output);
end.