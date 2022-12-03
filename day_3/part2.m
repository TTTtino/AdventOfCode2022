#import <Foundation/Foundation.h>

NSString* getCommonCharactersInStrings(NSString *stringA, NSString *stringB)
{   
    NSString* commonCharacters = @"";
    int i;
    int asciiA = 0;
    for (i = 0; i < [stringA length]; i++)
    {
        asciiA = [stringA characterAtIndex:i];
        NSString *key = [NSString stringWithFormat:@"%c", asciiA];
        if ([stringB rangeOfString:key].location != NSNotFound && [commonCharacters rangeOfString:key].location == NSNotFound){
            commonCharacters = [commonCharacters stringByAppendingString:key];
        }
    }
    return commonCharacters;
}

int asciiToValue(int ascii)
{
    if (ascii >= 97 && ascii <= 122){
        return (ascii - 96);
    }
    
    if (ascii >= 65 && ascii <= 90){
        return (ascii - 38);
    }
    return 0;
}

@interface Rucksack: NSObject
{
    NSString *compartmentA;
    NSString *compartmentB;
}

-(void) setContents: (NSString*) contents;
-(NSString*) getContents;
-(NSString*) stringifyRucksack;
-(int) getCommonCharacter;

@end

@implementation Rucksack

-(void) setContents: (NSString*) contents;
{
    NSUInteger len = contents.length;
    compartmentA = [contents substringToIndex:(len/2)];
    compartmentB = [contents substringFromIndex:(len/2)];
}

-(NSString*) getContents;
{
    return [compartmentA stringByAppendingString:compartmentB];
}

-(NSString*) stringifyRucksack;
{
    return [NSString stringWithFormat:@"CompartmentA: %@ | CompartmentB: %@", compartmentA, compartmentB];
}

-(int) getCommonCharacter;
{   

    return [getCommonCharactersInStrings(compartmentA, compartmentB) characterAtIndex:0];
}
@end

int getBadgeCharacter(NSMutableArray *rucksacks){
    
    NSString* commonChars =  getCommonCharactersInStrings([[rucksacks objectAtIndex: 0] getContents], [[rucksacks objectAtIndex: 1] getContents]);
    // NSLog(@"%@",commonChars);
    int i;
    int asciiA;
    for (i = 0; i < [commonChars length]; i++) {
        asciiA = [commonChars characterAtIndex:i];
        NSString *key = [NSString stringWithFormat:@"%c", asciiA];
        if ([[[rucksacks objectAtIndex: 2] getContents] rangeOfString:key].location != NSNotFound){
        
            // NSLog(@"%c", asciiA);
            return asciiA;
        }
    }
    return 0;
}


int main (int argc, const char * argv[])
{
    NSAutoreleasePool *pool = [[NSAutoreleasePool alloc] init];

    NSFileManager *fileManager = [NSFileManager defaultManager];
    
    if ([fileManager fileExistsAtPath:@"/uploads/input.txt"] == YES) {
       NSLog(@"File exists");
    }
    NSData *data = [fileManager contentsAtPath:@"/uploads/input.txt"];
    NSString *strData = [[NSString alloc]initWithData:data encoding:NSUTF8StringEncoding];
    


    NSArray *rucksacksstr = [strData componentsSeparatedByCharactersInSet: [NSCharacterSet newlineCharacterSet]];
    rucksacksstr = [rucksacksstr filteredArrayUsingPredicate: [NSPredicate predicateWithFormat:@"length > 0"]];
    
    int numOfRucksacks = [rucksacksstr count];
    int sum = 0;
    int i;
    
    NSMutableArray *group = [[NSMutableArray alloc] init];
    for (i = 0; i < numOfRucksacks; i++)
    {
        // NSLog(@"Rucksack %d: %@", i, [rucksacksstr objectAtIndex: i]);
        Rucksack *rucksack = [[Rucksack alloc] init];
        [rucksack setContents: [rucksacksstr objectAtIndex: i]];
        // NSLog(@"%@", [rucksack stringifyRucksack]);
        if (i % 3 == 0 && i != 0){
            sum += asciiToValue(getBadgeCharacter(group));
            [group removeAllObjects];
        }
        [group addObject:rucksack];
        
        
    }
    
    sum += asciiToValue(getBadgeCharacter(group));
    [group removeAllObjects];
    
    NSLog(@"%d", sum);
    
    [pool drain];    
    return 0; 
}