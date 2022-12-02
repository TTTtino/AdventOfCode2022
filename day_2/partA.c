#include <stdio.h>
#include <stdlib.h>

int getShapeScore(char p)
{
    int shapeScore = 0;
    switch (p)
    {
    case 'A':
    case 'X':
        shapeScore = 1;
        break;
    case 'B':
    case 'Y':
        shapeScore = 2;
        break;
    case 'C':
    case 'Z':
        shapeScore = 3;
        break;
    default:
        break;
    }

    return shapeScore;
}

//   X Y Z
// A 3 0 6
// B 6 3 0
// C 0 6 3

int outcome[3][3] = {{3, 0, 6}, {6, 3, 0}, {0, 6, 3}};

int getScore(char p1, char p2)
{
    int shapeScore = getShapeScore(p2);

    int shapeScoreOpponent = getShapeScore(p1);
    int winScore = outcome[shapeScore - 1][shapeScoreOpponent - 1];
    // printf("%c %c | shapeScore: %d | winScore: %d ", p1, p2, shapeScore, winScore);
    return shapeScore + winScore;
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