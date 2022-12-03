#import <Foundation/Foundation.h>

int getFirstCommonCharacterInStrings(NSString *stringA, NSString *stringB)
{   
    int i;
    int asciiA = 0;
    for (i = 0; i < [stringA length]; i++)
    {
        asciiA = [stringA characterAtIndex:i];
        NSString *key = [NSString stringWithFormat:@"%c", asciiA];
        if ([stringB rangeOfString:key].location != NSNotFound){
            return asciiA;
        }
    }
    return -1;
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
    return getFirstCommonCharacterInStrings(compartmentA, compartmentB);
}
@end




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
    
    
    for (i = 0; i < numOfRucksacks; i++)
    {
        // NSLog(@"Rucksack %d: %@", i, [rucksacksstr objectAtIndex: i]);
        Rucksack *rucksack = [[Rucksack alloc] init];
        [rucksack setContents: [rucksacksstr objectAtIndex: i]];
        // NSLog(@"%@ : %d", [rucksack stringifyRucksack], asciiToValue([rucksack getCommonCharacter]));
        sum += asciiToValue([rucksack getCommonCharacter]);
        [rucksack release];
        
    }
        
    NSLog(@"%d", sum);
    
    [pool drain];    
    return 0; 
} 