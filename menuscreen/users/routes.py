from flask import (render_template, url_for, flash, redirect,
                    request, Blueprint, jsonify)
from flask_login import (login_user, current_user, logout_user, login_required,
                            fresh_login_required)
from passlib.hash import sha256_crypt
from menuscreen import db
from menuscreen.models import User, List_history
from menuscreen.users.forms import (RegisterForm, LoginForm, UpdateAccountForm,
                                    RequestResetForm, ResetPasswordForm)
from menuscreen.users.utils import save_picture, send_reset_email, get_user_data

from menuscreen.users.init_db_tables import (getVenueId, initListHistory,
                                initListCurrent, initWinelist, initWinelistCurrent,
                                initWinetype, initBeerscreenSettings, initWinescreenSettings,
                                initEventscreenSettings, initItemscreenSettings,
                                initFontSizeOptions, initTemplate, initEvent, initItem,
                                initTicker, initTickerTypeId)


users = Blueprint('users', __name__)

@users.route('/_logged_in_user_data', methods=['GET', 'POST'])
# @login_required
def _logged_in_user_data():
    data = request.get_json()
    print("**************************************")
    print("******LINE  27************************")
    print("users. /_logged_in_user_data")
    print("**************************************")
    print("data: {}".format(data))
    print("**************************************")
    print("**************************************")
    if (current_user.is_authenticated):
        print("LOGGED IN")
        data['userId'] = current_user.id
        print("data: {}".format(data))
        data = get_user_data(data)

    elif (data):
        print("NOT LOGGED IN")
        print("data: {}".format(data))
        if (hasattr(data, 'userName')):
            print("data['userName']: {}".format(data['userName']))
            print("HASATTR")
        # try:
        #     attr = getattr(data, 'userName')
        #     print(attr)
        # except AttributeError:
        #     print ("DOESN'T EXIST")
        # else:
        #     print ("EXISTS")
        #     print(data['userName'])
        #     current_user_id = getVenueId(data['userName'])
        #     print(current_user_id)
        #
        #     data['userId'] = current_user_id
        #     print("data: {}".format(data))
        #     data = get_user_data(data)
    else:
        print("NOT LOGGED IN AND NO URL INFO")
        data = {}
    print("**************************************")
    print("**************************************")
    return jsonify(data)





# User Register
@users.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('list_history.beer_dashboard'))
    form = RegisterForm(request.form)
    if form.validate_on_submit():
        name = form.name.data
        venuename = form.venuename.data
        username = form.username.data
        websiteURL = form.websiteURL.data
        email = form.email.data
        password = sha256_crypt.encrypt(str(form.password.data))
        user = User(name=name, venue_name=venuename, websiteURL=websiteURL, email=email, username=username, password=password)
        db.session.add(user)
        db.session.commit()


        # init new venue DB for wine tables
        initListHistory(getVenueId(venuename))
        initListCurrent({"id":getVenueId(venuename), "screenId": ""})
        initWinelist(getVenueId(venuename))
        initWinelistCurrent(getVenueId(venuename))
        initWinetype(getVenueId(venuename))
        initBeerscreenSettings({"id":getVenueId(venuename), "screenId": ""})
        initWinescreenSettings(getVenueId(venuename))
        initEventscreenSettings(getVenueId(venuename))
        initItemscreenSettings(getVenueId(venuename))
        initFontSizeOptions(getVenueId(venuename))
        initTemplate(getVenueId(venuename))
        # initEvent(getVenueId(venuename))
        initItem(getVenueId(venuename))
        initTicker(getVenueId(venuename))
        initTickerTypeId(getVenueId(venuename))

        flash('{}, you are now registered and can log in!'.format(username), 'success')
        return redirect(url_for('users.login'))
    return render_template('register.html', title='Register', legend='Register', form=form)

# User login
@users.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('list_history.beer_dashboard'))
    form = LoginForm()
    if form.validate_on_submit():
        # Get Form Fields
        username = form.username.data
        password_candidate = form.password.data
        user = User.query.filter_by(username=username).first()
        if user:
            # Compare passwords
            if sha256_crypt.verify(password_candidate, user.password):
                login_user(user, remember=form.remember.data, force=True)
                next_page = request.args.get('next')
                flash('You are now logged in', 'success')
                return redirect(next_page) if next_page else redirect(url_for('list_history.beer_dashboard'))
            else:
                error = 'Invalid login'
                return render_template('login.html', title='Login', error=error, form=form)
        else:
            error = 'Username not found'
            return render_template('login.html', title='Login', error=error, form=form)
    return render_template('login.html', title='Login', legend='Login', form=form)

@users.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.home'))


@users.route('/account', methods=['GET', 'POST'])
@fresh_login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.name = form.name.data
        current_user.venue_name = form.venuename.data
        current_user.email = form.email.data
        current_user.username = form.username.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('users.account'))
    elif request.method == 'GET':
        form.name.data = current_user.name
        form.venuename.data = current_user.venue_name
        form.email.data = current_user.email
        form.username.data = current_user.username

    image_file = url_for('static', filename='img/profile_pics/' + current_user.image_file)
    return render_template('account.html', title='Account', legend='Account', image_file=image_file, form=form)


# Route for user to enter email to get link with a token to reset their password
# user can do this from the login screen and does not have to be logged in
@users.route('/reset_password', methods=['GET', 'POST'])
def reset_request():
    if current_user.is_authenticated:
        return redirect(url_for('list_history.dashboard'))
    form = RequestResetForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        send_reset_email(user)
        flash('An email has been sent with instructions to reset you password.', 'info')
        return redirect(url_for('users.login'))
    return render_template('reset_request.html', title='Reset Password', form=form)

# Route from email to create a new password and then confirm that password
@users.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_token(token):
    if current_user.is_authenticated:
        return redirect(url_for('list_history.dashboard'))
    user = User.verify_reset_token(token)
    if user is None:
        flash('That is an invalid or expired token', 'warning')
        return redirect(url_for('users.reset_request'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        hashed_password = sha256_crypt.encrypt(str(form.password.data))
        user.password = hashed_password
        db.session.commit()
        flash('{}, your password has been updated and can login!'.format(user.username), 'success')
        return redirect(url_for('users.login'))
    return render_template('reset_token.html', title='Reset Password', form=form)

# Route for user to change password while logged in
@users.route('/change_password', methods=['GET', 'POST'])
@fresh_login_required
def change_password():
    form = ResetPasswordForm()
    user = current_user
    if form.validate_on_submit():
        hashed_password = sha256_crypt.encrypt(str(form.password.data))
        user.password = hashed_password
        db.session.commit()
        flash('{}, your password has been updated and can login with the new password!'.format(user.username), 'success')
        return redirect(url_for('users.account'))
    return render_template('reset_token.html', title='Reset Password', form=form)
