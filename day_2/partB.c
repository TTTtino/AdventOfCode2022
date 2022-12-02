#include <stdio.h>
#include <stdlib.h>

int getShapeScore(char p)
{
    int shapeScore = 0;
    switch (p)
    {
    case 'A':
        shapeScore = 1;
        break;
    case 'B':
        shapeScore = 2;
        break;
    case 'C':
        shapeScore = 3;
        break;
    default:
        break;
    }

    return shapeScore;
}

int getResultValue(char result)
{
    int resultVal = 0;
    switch (result)
    {
    case 'X':
        resultVal = 0;
        break;
    case 'Y':
        resultVal = 1;
        break;
    case 'Z':
        resultVal = 2;
        break;
    default:
        break;
    }

    return resultVal;
}

// X: Lose 0   Y: Draw 3   Z:   Win 6
//   X Y Z
// A 3 1 2
// B 1 2 3
// C 2 3 1

int outcome[3][3] = {{3, 1, 2}, {1, 2, 3}, {2, 3, 1}};

int getScore(char p1, char p2)
{
    int resultVal = getResultValue(p2);
    int toPlay = outcome[getShapeScore(p1) - 1][resultVal];
    // printf("%c %c | result %d | toPlay %d | Score %d", p1, p2, resultVal * 3, toPlay, resultVal * 3 + toPlay);
    return resultVal * 3 + toPlay;
}

int main()
{
    FILE *fp = fopen("input.txt", "r");
    if (fp == NULL)
    {
        exit(1);
    }

    char line[2];
    int turn = 0;
    char p1 = ' ';
    int scoreSum = 0;
    while (fgets(line, sizeof(line), fp) != NULL)
    {
        if (line[0] != '\n' && line[0] != ' ')
        {

            if (turn == 0)
            {
                p1 = line[0];
                turn = 1;
            }
            else
            {
                scoreSum += getScore(p1, line[0]);
                turn = 0;
            }
        }
    }
    printf("Score Total: %d", scoreSum);
    fclose(fp);
}