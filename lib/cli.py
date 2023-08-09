from sqlalchemy import create_engine


engine = create_engine('sqlite:///recipe.db')

if __name__ == "__main__":
    print("welcome bitches")