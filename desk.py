from plyer import notification
import time

if __name__ == '__main__':
    while True:
        notification.notify(
            title="Take Rest",
            message=(
                "Hey Rutuja\n\n"
                "I hope your day is going well! I just wanted to remind you of the importance of taking breaks and giving yourself some time to recharge. "
                "Remember that constant work without breaks can lead to stress and burnout.\n\n"
                # "Take a moment to stretch, breathe, or even go for a short walk. Your well-being is essential, and taking breaks can actually boost productivity and creativity.\n\n"
                # "You've been doing great, and a short break now will help you come back even stronger.\n\n"
                "Best,\nYours Dency"
            ),
            # app_icon="https://static.vecteezy.com/system/resources/thumb…itting-on-chair-wait-concept-flat-icon-vector.jpg",
            timeout=5
        )
        time.sleep(3600)
