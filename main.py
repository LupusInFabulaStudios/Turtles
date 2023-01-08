import snowflake
import turtle

print(turtle.Screen())
snowflake.Snowflake((0,0)).DrawFlake(branches=5, length=30, multiplier=.5, layers=3, type=snowflake.SnowflakeTypes.Shrink)

snowflake.Snowflake((100,100)).DrawFlake(branches=6, length=10, multiplier=4, layers=2, type=snowflake.SnowflakeTypes.Wild)

while True:
    pass

