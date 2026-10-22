# main.py

from repositories.json_repository import JSONRepository
from services.library_service import LibraryService
from utils.exceptions import LibraryException

def main():
    repo = JSONRepository()
    service = LibraryService(repo)

    while True:
        print("\n" + "="*40)
        print(" 📚 Online Library Management System ")
        print("="*40)
        print("1. Add a New User")
        print("2. Add a New Book")
        print("3. Search for a Book")
        print("4. Borrow a Book")
        print("5. Rate a Book")
        print("6. Exit")
        print("="*40)
        
        choice = input("Enter your choice (1-6): ")
        
        try:
            if choice == '1':
                name = input("Enter user name: ")
                email = input("Enter user email: ")
                user = service.add_user(name, email)
                print(f"✅ User '{user.name}' added successfully with ID: {user.id}")
                
            elif choice == '2':
                title = input("Enter book title: ")
                author = input("Enter book author: ")
                cat_id = int(input("Enter category ID (e.g., 1): "))
                copies = int(input("Enter available copies: "))
                book = service.add_book(title, author, cat_id, copies)
                print(f"✅ Book '{book.title}' added successfully with ID: {book.id}")
                
            elif choice == '3':
                query = input("Enter title or author to search: ")
                results = service.search_books(query)
                if results:
                    print(f"\n🔍 Found {len(results)} books:")
                    for b in results:
                        avg_rating = service.get_book_average_rating(b.id)
                        print(f"- [ID: {b.id}] {b.title} by {b.author} | Copies: {b.available_copies} | ⭐ {avg_rating}/10")
                else:
                    print("❌ No books found matching your query.")
                    
            elif choice == '4':
                user_id = int(input("Enter User ID: "))
                book_id = int(input("Enter Book ID: "))
                if service.borrow_book(user_id, book_id):
                    print("✅ Book borrowed successfully! Copies updated.")
                    
            elif choice == '5':
                user_id = int(input("Enter User ID: "))
                book_id = int(input("Enter Book ID: "))
                score = float(input("Enter your rating (1-10): "))
                review = input("Enter a short review (optional): ")
                service.rate_book(user_id, book_id, score, review)
                
                new_avg = service.get_book_average_rating(book_id)
                print(f"✅ Rating added! New average for this book is: ⭐ {new_avg}/10")
                
            elif choice == '6':
                print("👋 Exiting the system. Goodbye!")
                break
                
            else:
                print("⚠️ Invalid choice. Please select a number from 1 to 6.")
                
        except ValueError:
            print("❌ Invalid input type! Please enter numbers where expected.")
        except LibraryException as e:
            print(f"⚠️ Business Rule Error: {e}")
        except Exception as e:
            print(f"🚨 Unexpected System Error: {e}")

if __name__ == "__main__":
    main()