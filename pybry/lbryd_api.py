"""
LBRY daemon wrapper in Python. Import it and initialize the main class.

This file was generated at build time using the `generator` module.
You may edit it but do so with caution.
If this file contains syntax errors, check the input file
for badly formated fields.
Input JSON: https://raw.githubusercontent.com/lbryio/lbry/master/docs/api.json
"""
from pybry.base_api import BaseApi
from pybry.constants import LBRYD_SERVER_ADDRESS as SERVER_ADDRESS


class LbrydApi(BaseApi):

    def __init__(self, timeout=600):
        """
        LBRY daemon wrapper.

        Initialize this class, and use its methods.
        >>> lbry = LbrydApi()
        >>> response = lbry.claim_search(name='LBRYPlaylists')

        :param float timeout: The number of seconds to wait for a connection until we time out
        """
        self.timeout = timeout

    @classmethod
    def call(cls, method, params=None, timeout=600):
        """Makes a call to the LBRY API.

        :param str method: Method to call from the LBRY API. See the full list of methods at
         https://github.com/lbryio/lbry-sdk/blob/master/lbry/extras/daemon/daemon.py
         The daemon methods start with the string `jsonrpc_`
        :param dict params: Parameters to give the method selected
        :param float timeout: The number of seconds to wait for a connection until we time out; 600 By Default.
        :raises LBRYException: If the request returns an error when calling the API
        :return: A Python `dict` object containing the data requested from the API
        :rtype: dict
        """

        params = [] if params is None else params

        return cls.make_request(SERVER_ADDRESS, method, params, timeout=timeout)

    def ffmpeg_find(self):
        """Get ffmpeg installation information

        """
        __params_map = {}

        return self.make_request(SERVER_ADDRESS, 'ffmpeg_find', __params_map, timeout=self.timeout)

    def get(self, uri=None, file_name=None, download_directory=None, timeout=None, save_file=None, wallet_id=None):
        """Download stream from a LBRY name.

        :param str uri: uri of the content to download (Optional)
        :param str file_name: specified name for the downloaded file, overrides the stream file name (Optional)
        :param str download_directory: full path to the directory to download into (Optional)
        :param int timeout: download timeout in number of seconds (Optional)
        :param bool save_file: save the file to the downloads directory (Optional)
        :param str wallet_id: wallet to check for claim purchase receipts (Optional)
        """
        __params_map = {'uri': uri,
                        'file_name': file_name,
                        'download_directory': download_directory,
                        'timeout': timeout,
                        'save_file': save_file,
                        'wallet_id': wallet_id}

        return self.make_request(SERVER_ADDRESS, 'get', __params_map, timeout=self.timeout)

    def publish(self, name, bid=None, file_path=None, file_name=None, file_hash=None, validate_file=None, optimize_file=None, fee_currency=None, fee_amount=None, fee_address=None, title=None, description=None, author=None, tags=None, languages=None, locations=None, license=None, license_url=None, thumbnail_url=None, release_time=None, width=None, height=None, duration=None, sd_hash=None, channel_id=None, channel_name=None, channel_account_id=None, account_id=None, wallet_id=None, funding_account_ids=None, claim_address=None, preview=None, blocking=None):
        """Create or replace a stream claim at a given name (use 'stream create/update' for more control).

        :param str name: name of the content (can only consist of a-z A-Z 0-9 and -(dash))
        :param float bid: amount to back the claim (Optional)
        :param str file_path: path to file to be associated with name. (Optional)
        :param str file_name: name of file to be associated with stream. (Optional)
        :param str file_hash: hash of file to be associated with stream. (Optional)
        :param bool validate_file: validate that the video container and encodings match common web browser support or that optimization succeeds if specified. FFmpeg is required (Optional)
        :param bool optimize_file: transcode the video & audio if necessary to ensure common web browser support. FFmpeg is required (Optional)
        :param str fee_currency: specify fee currency (Optional)
        :param float fee_amount: content download fee (Optional)
        :param str fee_address: address where to send fee payments, will use value from --claim_address if not provided (Optional)
        :param str title: title of the publication (Optional)
        :param str description: description of the publication (Optional)
        :param str author: author of the publication. The usage for this field is not the same as for channels. The author field is used to credit an author who is not the publisher and is not represented by the channel. For example, a pdf file of 'The Odyssey' has an author of 'Homer' but may by published to a channel such as '@classics', or to no channel at all (Optional)
        :param list tags: add content tags (Optional)
        :param list languages: languages used by the channel, using RFC 5646 format, eg: for English `--languages=en` for Spanish (Spain) `--languages=es-ES` for Spanish (Mexican) `--languages=es-MX` for Chinese (Simplified) `--languages=zh-Hans` for Chinese (Traditional) `--languages=zh-Hant` (Optional)
        :param list locations: locations relevant to the stream, consisting of 2 letter `country` code and a `state`, `city` and a postal `code` along with a `latitude` and `longitude`. for JSON RPC: pass a dictionary with aforementioned attributes as keys, eg: ... "locations": [{'country': 'US', 'state': 'NH'}] ... for command line: pass a colon delimited list with values in the following order: "COUNTRY:STATE:CITY:CODE:LATITUDE:LONGITUDE" making sure to include colon for blank values, for example to provide only the city: ... --locations="::Manchester" with all values set: ... --locations="US:NH:Manchester:03101:42.990605:-71.460989" optionally, you can just pass the "LATITUDE:LONGITUDE": ... --locations="42.990605:-71.460989" finally, you can also pass JSON string of dictionary on the command line as you would via JSON RPC ... --locations="{'country': 'US', 'state': 'NH'}" (Optional)
        :param str license: publication license (Optional)
        :param str license_url: publication license url (Optional)
        :param str thumbnail_url: thumbnail url (Optional)
        :param int release_time: original public release of content, seconds since UNIX epoch (Optional)
        :param int width: image/video width, automatically calculated from media file (Optional)
        :param int height: image/video height, automatically calculated from media file (Optional)
        :param int duration: audio/video duration in seconds, automatically calculated (Optional)
        :param str sd_hash: sd_hash of stream (Optional)
        :param str channel_id: claim id of the publisher channel (Optional)
        :param str channel_name: name of publisher channel (Optional)
        :param str channel_account_id: one or more account ids for accounts to look in for channel certificates, defaults to all accounts. (Optional)
        :param str account_id: account to use for holding the transaction (Optional)
        :param str wallet_id: restrict operation to specific wallet (Optional)
        :param list funding_account_ids: ids of accounts to fund this transaction (Optional)
        :param str claim_address: address where the claim is sent to, if not specified it will be determined automatically from the account (Optional)
        :param bool preview: do not broadcast the transaction (Optional)
        :param bool blocking: wait until transaction is in mempool (Optional)
        """
        __params_map = {'name': name,
                        'bid': bid,
                        'file_path': file_path,
                        'file_name': file_name,
                        'file_hash': file_hash,
                        'validate_file': validate_file,
                        'optimize_file': optimize_file,
                        'fee_currency': fee_currency,
                        'fee_amount': fee_amount,
                        'fee_address': fee_address,
                        'title': title,
                        'description': description,
                        'author': author,
                        'tags': tags,
                        'languages': languages,
                        'locations': locations,
                        'license': license,
                        'license_url': license_url,
                        'thumbnail_url': thumbnail_url,
                        'release_time': release_time,
                        'width': width,
                        'height': height,
                        'duration': duration,
                        'sd_hash': sd_hash,
                        'channel_id': channel_id,
                        'channel_name': channel_name,
                        'channel_account_id': channel_account_id,
                        'account_id': account_id,
                        'wallet_id': wallet_id,
                        'funding_account_ids': funding_account_ids,
                        'claim_address': claim_address,
                        'preview': preview,
                        'blocking': blocking}

        return self.make_request(SERVER_ADDRESS, 'publish', __params_map, timeout=self.timeout)

    def resolve(self, urls=None, wallet_id=None, new_sdk_server=None, include_purchase_receipt=None, include_is_my_output=None, include_sent_supports=None, include_sent_tips=None, include_received_tips=None):
        """Get the claim that a URL refers to.

        :param list urls: one or more urls to resolve (Optional)
        :param str wallet_id: wallet to check for claim purchase receipts (Optional)
        :param str new_sdk_server: URL of the new SDK server (EXPERIMENTAL) (Optional)
        :param bool include_purchase_receipt: lookup and include a receipt if this wallet has purchased the claim being resolved (Optional)
        :param bool include_is_my_output: lookup and include a boolean indicating if claim being resolved is yours (Optional)
        :param bool include_sent_supports: lookup and sum the total amount of supports you've made to this claim (Optional)
        :param bool include_sent_tips: lookup and sum the total amount of tips you've made to this claim (only makes sense when claim is not yours) (Optional)
        :param bool include_received_tips: lookup and sum the total amount of tips you've received to this claim (only makes sense when claim is yours) (Optional)
        """
        __params_map = {'urls': urls,
                        'wallet_id': wallet_id,
                        'new_sdk_server': new_sdk_server,
                        'include_purchase_receipt': include_purchase_receipt,
                        'include_is_my_output': include_is_my_output,
                        'include_sent_supports': include_sent_supports,
                        'include_sent_tips': include_sent_tips,
                        'include_received_tips': include_received_tips}

        return self.make_request(SERVER_ADDRESS, 'resolve', __params_map, timeout=self.timeout)

    def routing_table_get(self):
        """Get DHT routing information

        """
        __params_map = {}

        return self.make_request(SERVER_ADDRESS, 'routing_table_get', __params_map, timeout=self.timeout)

    def status(self):
        """Get daemon status

        """
        __params_map = {}

        return self.make_request(SERVER_ADDRESS, 'status', __params_map, timeout=self.timeout)

    def stop(self):
        """Stop lbrynet API server.

        """
        __params_map = {}

        return self.make_request(SERVER_ADDRESS, 'stop', __params_map, timeout=self.timeout)

    def version(self):
        """Get lbrynet API server version information

        """
        __params_map = {}

        return self.make_request(SERVER_ADDRESS, 'version', __params_map, timeout=self.timeout)

    def account_add(self, account_name, seed=None, private_key=None, public_key=None, single_key=None, wallet_id=None):
        """Add a previously created account from a seed, private key or public key (read-only).
Specify --single_key for single address or vanity address accounts.

        :param str account_name: name of the account to add
        :param str seed: seed to generate new account from (Optional)
        :param str private_key: private key for new account (Optional)
        :param str public_key: public key for new account (Optional)
        :param bool single_key: create single key account, default is multi-key (Optional)
        :param str wallet_id: restrict operation to specific wallet (Optional)
        """
        __params_map = {'account_name': account_name,
                        'seed': seed,
                        'private_key': private_key,
                        'public_key': public_key,
                        'single_key': single_key,
                        'wallet_id': wallet_id}

        return self.make_request(SERVER_ADDRESS, 'account_add', __params_map, timeout=self.timeout)

    def account_balance(self, account_id=None, wallet_id=None, confirmations=None):
        """Return the balance of an account

        :param str account_id: If provided only the balance for this account will be given. Otherwise default account. (Optional)
        :param str wallet_id: balance for specific wallet (Optional)
        :param int confirmations: Only include transactions with this many confirmed blocks. (Optional)
        """
        __params_map = {'account_id': account_id,
                        'wallet_id': wallet_id,
                        'confirmations': confirmations}

        return self.make_request(SERVER_ADDRESS, 'account_balance', __params_map, timeout=self.timeout)

    def account_create(self, account_name, single_key=None, wallet_id=None):
        """Create a new account. Specify --single_key if you want to use
the same address for all transactions (not recommended).

        :param str account_name: name of the account to create
        :param bool single_key: create single key account, default is multi-key (Optional)
        :param str wallet_id: restrict operation to specific wallet (Optional)
        """
        __params_map = {'account_name': account_name,
                        'single_key': single_key,
                        'wallet_id': wallet_id}

        return self.make_request(SERVER_ADDRESS, 'account_create', __params_map, timeout=self.timeout)

    def account_deposit(self, txid=None, nout=None, redeem_script=None, private_key=None, to_account=None, wallet_id=None, preview=None, blocking=None):
        """Spend a time locked transaction into your account.

        :param str txid: id of the transaction (Optional)
        :param int nout: output number in the transaction (Optional)
        :param str redeem_script: redeem script for output (Optional)
        :param str private_key: private key to sign transaction (Optional)
        :param str to_account: deposit to this account (Optional)
        :param str wallet_id: limit operation to specific wallet. (Optional)
        :param bool preview: do not broadcast the transaction (Optional)
        :param bool blocking: wait until tx has synced (Optional)
        """
        __params_map = {'txid': txid,
                        'nout': nout,
                        'redeem_script': redeem_script,
                        'private_key': private_key,
                        'to_account': to_account,
                        'wallet_id': wallet_id,
                        'preview': preview,
                        'blocking': blocking}

        return self.make_request(SERVER_ADDRESS, 'account_deposit', __params_map, timeout=self.timeout)

    def account_fund(self, amount, to_account=None, from_account=None, everything=None, outputs=None, wallet_id=None, broadcast=None):
        """Transfer some amount (or --everything) to an account from another
account (can be the same account). Amounts are interpreted as LBC.
You can also spread the transfer across a number of --outputs (cannot
be used together with --everything).

        :param float amount: the amount to transfer lbc
        :param str to_account: send to this account (Optional)
        :param str from_account: spend from this account (Optional)
        :param bool everything: transfer everything (excluding claims), default: false. (Optional)
        :param int outputs: split payment across many outputs, default: 1. (Optional)
        :param str wallet_id: limit operation to specific wallet. (Optional)
        :param bool broadcast: actually broadcast the transaction, default: false. (Optional)
        """
        __params_map = {'amount': amount,
                        'to_account': to_account,
                        'from_account': from_account,
                        'everything': everything,
                        'outputs': outputs,
                        'wallet_id': wallet_id,
                        'broadcast': broadcast}

        return self.make_request(SERVER_ADDRESS, 'account_fund', __params_map, timeout=self.timeout)

    def account_list(self, account_id=None, wallet_id=None, confirmations=None, include_claims=None, show_seed=None, page=None, page_size=None):
        """List details of all of the accounts or a specific account.

        :param str account_id: If provided only the balance for this account will be given (Optional)
        :param str wallet_id: accounts in specific wallet (Optional)
        :param int confirmations: required confirmations (default: 0) (Optional)
        :param bool include_claims: include claims, requires than a LBC account is specified (default: false) (Optional)
        :param bool show_seed: show the seed for the account (Optional)
        :param int page: page to return during paginating (Optional)
        :param int page_size: number of items on page during pagination (Optional)
        """
        __params_map = {'account_id': account_id,
                        'wallet_id': wallet_id,
                        'confirmations': confirmations,
                        'include_claims': include_claims,
                        'show_seed': show_seed,
                        'page': page,
                        'page_size': page_size}

        return self.make_request(SERVER_ADDRESS, 'account_list', __params_map, timeout=self.timeout)

    def account_max_address_gap(self, account_id, wallet_id=None):
        """Finds ranges of consecutive addresses that are unused and returns the length
of the longest such range: for change and receiving address chains. This is
useful to figure out ideal values to set for 'receiving_gap' and 'change_gap'
account settings.

        :param str account_id: account for which to get max gaps
        :param str wallet_id: restrict operation to specific wallet (Optional)
        """
        __params_map = {'account_id': account_id,
                        'wallet_id': wallet_id}

        return self.make_request(SERVER_ADDRESS, 'account_max_address_gap', __params_map, timeout=self.timeout)

    def account_remove(self, account_id, wallet_id=None):
        """Remove an existing account.

        :param str account_id: id of the account to remove
        :param str wallet_id: restrict operation to specific wallet (Optional)
        """
        __params_map = {'account_id': account_id,
                        'wallet_id': wallet_id}

        return self.make_request(SERVER_ADDRESS, 'account_remove', __params_map, timeout=self.timeout)

    def account_send(self, account_id=None, wallet_id=None, preview=None, blocking=None):
        """Send the same number of credits to multiple addresses from a specific account (or default account).

        :param str account_id: account to fund the transaction (Optional)
        :param str wallet_id: restrict operation to specific wallet (Optional)
        :param bool preview: do not broadcast the transaction (Optional)
        :param bool blocking: wait until tx has synced (Optional)
        """
        __params_map = {'account_id': account_id,
                        'wallet_id': wallet_id,
                        'preview': preview,
                        'blocking': blocking}

        return self.make_request(SERVER_ADDRESS, 'account_send', __params_map, timeout=self.timeout)

    def account_set(self, account_id, wallet_id=None, default=None, new_name=None, receiving_gap=None, receiving_max_uses=None, change_gap=None, change_max_uses=None):
        """Change various settings on an account.

        :param str account_id: id of the account to change
        :param str wallet_id: restrict operation to specific wallet (Optional)
        :param bool default: make this account the default (Optional)
        :param str new_name: new name for the account (Optional)
        :param int receiving_gap: set the gap for receiving addresses (Optional)
        :param int receiving_max_uses: set the maximum number of times to use a receiving address (Optional)
        :param int change_gap: set the gap for change addresses (Optional)
        :param int change_max_uses: set the maximum number of times to use a change address (Optional)
        """
        __params_map = {'account_id': account_id,
                        'wallet_id': wallet_id,
                        'default': default,
                        'new_name': new_name,
                        'receiving_gap': receiving_gap,
                        'receiving_max_uses': receiving_max_uses,
                        'change_gap': change_gap,
                        'change_max_uses': change_max_uses}

        return self.make_request(SERVER_ADDRESS, 'account_set', __params_map, timeout=self.timeout)

    def address_is_mine(self, address, account_id=None, wallet_id=None):
        """Checks if an address is associated with the current wallet.

        :param str address: address to check
        :param str account_id: id of the account to use (Optional)
        :param str wallet_id: restrict operation to specific wallet (Optional)
        """
        __params_map = {'address': address,
                        'account_id': account_id,
                        'wallet_id': wallet_id}

        return self.make_request(SERVER_ADDRESS, 'address_is_mine', __params_map, timeout=self.timeout)

    def address_list(self, address=None, account_id=None, wallet_id=None, page=None, page_size=None):
        """List account addresses or details of single address.

        :param str address: just show details for single address (Optional)
        :param str account_id: id of the account to use (Optional)
        :param str wallet_id: restrict operation to specific wallet (Optional)
        :param int page: page to return during paginating (Optional)
        :param int page_size: number of items on page during pagination (Optional)
        """
        __params_map = {'address': address,
                        'account_id': account_id,
                        'wallet_id': wallet_id,
                        'page': page,
                        'page_size': page_size}

        return self.make_request(SERVER_ADDRESS, 'address_list', __params_map, timeout=self.timeout)

    def address_unused(self, account_id=None, wallet_id=None):
        """Return an address containing no balance, will create
a new address if there is none.

        :param str account_id: id of the account to use (Optional)
        :param str wallet_id: restrict operation to specific wallet (Optional)
        """
        __params_map = {'account_id': account_id,
                        'wallet_id': wallet_id}

        return self.make_request(SERVER_ADDRESS, 'address_unused', __params_map, timeout=self.timeout)

    def blob_announce(self, blob_hash=None, stream_hash=None, sd_hash=None):
        """Announce blobs to the DHT

        :param str blob_hash: announce a blob, specified by blob_hash (Optional)
        :param str stream_hash: announce all blobs associated with stream_hash (Optional)
        :param str sd_hash: announce all blobs associated with sd_hash and the sd_hash itself (Optional)
        """
        __params_map = {'blob_hash': blob_hash,
                        'stream_hash': stream_hash,
                        'sd_hash': sd_hash}

        return self.make_request(SERVER_ADDRESS, 'blob_announce', __params_map, timeout=self.timeout)

    def blob_clean(self):
        """Deletes blobs to cleanup disk space

        """
        __params_map = {}

        return self.make_request(SERVER_ADDRESS, 'blob_clean', __params_map, timeout=self.timeout)

    def blob_delete(self, blob_hash):
        """Delete a blob

        :param str blob_hash: blob hash of the blob to delete
        """
        __params_map = {'blob_hash': blob_hash}

        return self.make_request(SERVER_ADDRESS, 'blob_delete', __params_map, timeout=self.timeout)

    def blob_get(self, blob_hash, timeout=None):
        """Download and return a blob

        :param str blob_hash: blob hash of the blob to get
        :param int timeout: timeout in number of seconds (Optional)
        """
        __params_map = {'blob_hash': blob_hash,
                        'timeout': timeout}

        return self.make_request(SERVER_ADDRESS, 'blob_get', __params_map, timeout=self.timeout)

    def blob_list(self, needed=None, finished=None, uri=None, stream_hash=None, sd_hash=None, page=None, page_size=None):
        """Returns blob hashes. If not given filters, returns all blobs known by the blob manager

        :param bool needed: only return needed blobs (Optional)
        :param bool finished: only return finished blobs (Optional)
        :param str uri: filter blobs by stream in a uri (Optional)
        :param str stream_hash: filter blobs by stream hash (Optional)
        :param str sd_hash: filter blobs in a stream by sd hash, ie the hash of the stream descriptor blob for a stream that has been downloaded (Optional)
        :param int page: page to return during paginating (Optional)
        :param int page_size: number of items on page during pagination (Optional)
        """
        __params_map = {'needed': needed,
                        'finished': finished,
                        'uri': uri,
                        'stream_hash': stream_hash,
                        'sd_hash': sd_hash,
                        'page': page,
                        'page_size': page_size}

        return self.make_request(SERVER_ADDRESS, 'blob_list', __params_map, timeout=self.timeout)

    def blob_reflect(self, reflector_server=None):
        """Reflects specified blobs

        :param str reflector_server: reflector address (Optional)
        """
        __params_map = {'reflector_server': reflector_server}

        return self.make_request(SERVER_ADDRESS, 'blob_reflect', __params_map, timeout=self.timeout)

    def blob_reflect_all(self):
        """Reflects all saved blobs

        """
        __params_map = {}

        return self.make_request(SERVER_ADDRESS, 'blob_reflect_all', __params_map, timeout=self.timeout)

    def channel_abandon(self, claim_id=None, txid=None, nout=None, account_id=None, wallet_id=None, preview=None, blocking=None):
        """Abandon one of my channel claims.

        :param str claim_id: claim_id of the claim to abandon (Optional)
        :param str txid: txid of the claim to abandon (Optional)
        :param int nout: nout of the claim to abandon (Optional)
        :param str account_id: id of the account to use (Optional)
        :param str wallet_id: restrict operation to specific wallet (Optional)
        :param bool preview: do not broadcast the transaction (Optional)
        :param bool blocking: wait until abandon is in mempool (Optional)
        """
        __params_map = {'claim_id': claim_id,
                        'txid': txid,
                        'nout': nout,
                        'account_id': account_id,
                        'wallet_id': wallet_id,
                        'preview': preview,
                        'blocking': blocking}

        return self.make_request(SERVER_ADDRESS, 'channel_abandon', __params_map, timeout=self.timeout)

    def channel_create(self, name, bid, allow_duplicate_name=None, title=None, description=None, email=None, website_url=None, featured=None, tags=None, languages=None, locations=None, thumbnail_url=None, cover_url=None, account_id=None, wallet_id=None, funding_account_ids=None, claim_address=None, preview=None, blocking=None):
        """Create a new channel by generating a channel private key and establishing an '@' prefixed claim.

        :param str name: name of the channel prefixed with '@'
        :param float bid: amount to back the claim
        :param bool allow_duplicate_name: create new channel even if one already exists with given name. default: false. (Optional)
        :param str title: title of the publication (Optional)
        :param str description: description of the publication (Optional)
        :param str email: email of channel owner (Optional)
        :param str website_url: website url (Optional)
        :param list featured: claim_ids of featured content in channel (Optional)
        :param list tags: content tags (Optional)
        :param list languages: languages used by the channel, using RFC 5646 format, eg: for English `--languages=en` for Spanish (Spain) `--languages=es-ES` for Spanish (Mexican) `--languages=es-MX` for Chinese (Simplified) `--languages=zh-Hans` for Chinese (Traditional) `--languages=zh-Hant` (Optional)
        :param list locations: locations of the channel, consisting of 2 letter `country` code and a `state`, `city` and a postal `code` along with a `latitude` and `longitude`. for JSON RPC: pass a dictionary with aforementioned attributes as keys, eg: ... "locations": [{'country': 'US', 'state': 'NH'}] ... for command line: pass a colon delimited list with values in the following order: "COUNTRY:STATE:CITY:CODE:LATITUDE:LONGITUDE" making sure to include colon for blank values, for example to provide only the city: ... --locations="::Manchester" with all values set: ... --locations="US:NH:Manchester:03101:42.990605:-71.460989" optionally, you can just pass the "LATITUDE:LONGITUDE": ... --locations="42.990605:-71.460989" finally, you can also pass JSON string of dictionary on the command line as you would via JSON RPC ... --locations="{'country': 'US', 'state': 'NH'}" (Optional)
        :param str thumbnail_url: thumbnail url (Optional)
        :param str cover_url: url of cover image (Optional)
        :param str account_id: account to use for holding the transaction (Optional)
        :param str wallet_id: restrict operation to specific wallet (Optional)
        :param list funding_account_ids: ids of accounts to fund this transaction (Optional)
        :param str claim_address: address where the channel is sent to, if not specified it will be determined automatically from the account (Optional)
        :param bool preview: do not broadcast the transaction (Optional)
        :param bool blocking: wait until transaction is in mempool (Optional)
        """
        __params_map = {'name': name,
                        'bid': bid,
                        'allow_duplicate_name': allow_duplicate_name,
                        'title': title,
                        'description': description,
                        'email': email,
                        'website_url': website_url,
                        'featured': featured,
                        'tags': tags,
                        'languages': languages,
                        'locations': locations,
                        'thumbnail_url': thumbnail_url,
                        'cover_url': cover_url,
                        'account_id': account_id,
                        'wallet_id': wallet_id,
                        'funding_account_ids': funding_account_ids,
                        'claim_address': claim_address,
                        'preview': preview,
                        'blocking': blocking}

        return self.make_request(SERVER_ADDRESS, 'channel_create', __params_map, timeout=self.timeout)

    def channel_export(self, channel_id, channel_name=None, account_id=None, wallet_id=None):
        """Export channel private key.

        :param str channel_id: claim id of channel to export
        :param str channel_name: name of channel to export (Optional)
        :param str account_id: one or more account ids for accounts to look in for channels, defaults to all accounts. (Optional)
        :param str wallet_id: restrict operation to specific wallet (Optional)
        """
        __params_map = {'channel_id': channel_id,
                        'channel_name': channel_name,
                        'account_id': account_id,
                        'wallet_id': wallet_id}

        return self.make_request(SERVER_ADDRESS, 'channel_export', __params_map, timeout=self.timeout)

    def channel_import(self, channel_data, wallet_id=None):
        """Import serialized channel private key (to allow signing new streams to the channel)

        :param str channel_data: serialized channel, as exported by channel export
        :param str wallet_id: import into specific wallet (Optional)
        """
        __params_map = {'channel_data': channel_data,
                        'wallet_id': wallet_id}

        return self.make_request(SERVER_ADDRESS, 'channel_import', __params_map, timeout=self.timeout)

    def channel_list(self, name=None, claim_id=None, is_spent=None, account_id=None, wallet_id=None, page=None, page_size=None, resolve=None, no_totals=None):
        """List my channel claims.

        :param list name: channel name (Optional)
        :param list claim_id: channel id (Optional)
        :param bool is_spent: shows previous channel updates and abandons (Optional)
        :param str account_id: id of the account to use (Optional)
        :param str wallet_id: restrict results to specific wallet (Optional)
        :param int page: page to return during paginating (Optional)
        :param int page_size: number of items on page during pagination (Optional)
        :param bool resolve: resolves each channel to provide additional metadata (Optional)
        :param bool no_totals: do not calculate the total number of pages and items in result set (significant performance boost) (Optional)
        """
        __params_map = {'name': name,
                        'claim_id': claim_id,
                        'is_spent': is_spent,
                        'account_id': account_id,
                        'wallet_id': wallet_id,
                        'page': page,
                        'page_size': page_size,
                        'resolve': resolve,
                        'no_totals': no_totals}

        return self.make_request(SERVER_ADDRESS, 'channel_list', __params_map, timeout=self.timeout)

    def channel_sign(self, channel_name=None, channel_id=None, hexdata=None, channel_account_id=None, wallet_id=None):
        """Signs data using the specified channel signing key.

        :param str channel_name: name of channel used to sign (or use channel id) (Optional)
        :param str channel_id: claim id of channel used to sign (or use channel name) (Optional)
        :param str hexdata: data to sign, encoded as hexadecimal (Optional)
        :param str channel_account_id: one or more account ids for accounts to look in for channel certificates, defaults to all accounts. (Optional)
        :param str wallet_id: restrict operation to specific wallet (Optional)
        """
        __params_map = {'channel_name': channel_name,
                        'channel_id': channel_id,
                        'hexdata': hexdata,
                        'channel_account_id': channel_account_id,
                        'wallet_id': wallet_id}

        return self.make_request(SERVER_ADDRESS, 'channel_sign', __params_map, timeout=self.timeout)

    def channel_update(self, claim_id, bid=None, title=None, description=None, email=None, website_url=None, featured=None, clear_featured=None, tags=None, clear_tags=None, languages=None, clear_languages=None, locations=None, clear_locations=None, thumbnail_url=None, cover_url=None, account_id=None, wallet_id=None, funding_account_ids=None, claim_address=None, new_signing_key=None, preview=None, blocking=None, replace=None):
        """Update an existing channel claim.

        :param str claim_id: claim_id of the channel to update
        :param float bid: amount to back the claim (Optional)
        :param str title: title of the publication (Optional)
        :param str description: description of the publication (Optional)
        :param str email: email of channel owner (Optional)
        :param str website_url: website url (Optional)
        :param list featured: claim_ids of featured content in channel (Optional)
        :param bool clear_featured: clear existing featured content (prior to adding new ones) (Optional)
        :param list tags: add content tags (Optional)
        :param bool clear_tags: clear existing tags (prior to adding new ones) (Optional)
        :param list languages: languages used by the channel, using RFC 5646 format, eg: for English `--languages=en` for Spanish (Spain) `--languages=es-ES` for Spanish (Mexican) `--languages=es-MX` for Chinese (Simplified) `--languages=zh-Hans` for Chinese (Traditional) `--languages=zh-Hant` (Optional)
        :param bool clear_languages: clear existing languages (prior to adding new ones) (Optional)
        :param list locations: locations of the channel, consisting of 2 letter `country` code and a `state`, `city` and a postal `code` along with a `latitude` and `longitude`. for JSON RPC: pass a dictionary with aforementioned attributes as keys, eg: ... "locations": [{'country': 'US', 'state': 'NH'}] ... for command line: pass a colon delimited list with values in the following order: "COUNTRY:STATE:CITY:CODE:LATITUDE:LONGITUDE" making sure to include colon for blank values, for example to provide only the city: ... --locations="::Manchester" with all values set: ... --locations="US:NH:Manchester:03101:42.990605:-71.460989" optionally, you can just pass the "LATITUDE:LONGITUDE": ... --locations="42.990605:-71.460989" finally, you can also pass JSON string of dictionary on the command line as you would via JSON RPC ... --locations="{'country': 'US', 'state': 'NH'}" (Optional)
        :param bool clear_locations: clear existing locations (prior to adding new ones) (Optional)
        :param str thumbnail_url: thumbnail url (Optional)
        :param str cover_url: url of cover image (Optional)
        :param str account_id: account in which to look for channel (default: all) (Optional)
        :param str wallet_id: restrict operation to specific wallet (Optional)
        :param list funding_account_ids: ids of accounts to fund this transaction (Optional)
        :param str claim_address: address where the channel is sent (Optional)
        :param bool new_signing_key: generate a new signing key, will invalidate all previous publishes (Optional)
        :param bool preview: do not broadcast the transaction (Optional)
        :param bool blocking: wait until transaction is in mempool (Optional)
        :param bool replace: instead of modifying specific values on the channel, this will clear all existing values and only save passed in values, useful for form submissions where all values are always set (Optional)
        """
        __params_map = {'claim_id': claim_id,
                        'bid': bid,
                        'title': title,
                        'description': description,
                        'email': email,
                        'website_url': website_url,
                        'featured': featured,
                        'clear_featured': clear_featured,
                        'tags': tags,
                        'clear_tags': clear_tags,
                        'languages': languages,
                        'clear_languages': clear_languages,
                        'locations': locations,
                        'clear_locations': clear_locations,
                        'thumbnail_url': thumbnail_url,
                        'cover_url': cover_url,
                        'account_id': account_id,
                        'wallet_id': wallet_id,
                        'funding_account_ids': funding_account_ids,
                        'claim_address': claim_address,
                        'new_signing_key': new_signing_key,
                        'preview': preview,
                        'blocking': blocking,
                        'replace': replace}

        return self.make_request(SERVER_ADDRESS, 'channel_update', __params_map, timeout=self.timeout)

    def claim_list(self, claim_type=None, claim_id=None, channel_id=None, name=None, is_spent=None, account_id=None, wallet_id=None, has_source=None, has_no_source=None, page=None, page_size=None, resolve=None, order_by=None, no_totals=None, include_received_tips=None):
        """List my stream and channel claims.

        :param list claim_type: claim type: channel, stream, repost, collection (Optional)
        :param list claim_id: claim id (Optional)
        :param list channel_id: streams in this channel (Optional)
        :param list name: claim name (Optional)
        :param bool is_spent: shows previous claim updates and abandons (Optional)
        :param str account_id: id of the account to query (Optional)
        :param str wallet_id: restrict results to specific wallet (Optional)
        :param bool has_source: list claims containing a source field (Optional)
        :param bool has_no_source: list claims not containing a source field (Optional)
        :param int page: page to return during paginating (Optional)
        :param int page_size: number of items on page during pagination (Optional)
        :param bool resolve: resolves each claim to provide additional metadata (Optional)
        :param str order_by: field to order by: 'name', 'height', 'amount' (Optional)
        :param bool no_totals: do not calculate the total number of pages and items in result set (significant performance boost) (Optional)
        :param bool include_received_tips: calculate the amount of tips received for claim outputs (Optional)
        """
        __params_map = {'claim_type': claim_type,
                        'claim_id': claim_id,
                        'channel_id': channel_id,
                        'name': name,
                        'is_spent': is_spent,
                        'account_id': account_id,
                        'wallet_id': wallet_id,
                        'has_source': has_source,
                        'has_no_source': has_no_source,
                        'page': page,
                        'page_size': page_size,
                        'resolve': resolve,
                        'order_by': order_by,
                        'no_totals': no_totals,
                        'include_received_tips': include_received_tips}

        return self.make_request(SERVER_ADDRESS, 'claim_list', __params_map, timeout=self.timeout)

    def claim_search(self, name=None, text=None, claim_id=None, claim_ids=None, txid=None, nout=None, channel=None, channel_ids=None, not_channel_ids=None, has_channel_signature=None, valid_channel_signature=None, invalid_channel_signature=None, limit_claims_per_channel=None, is_controlling=None, public_key_id=None, height=None, timestamp=None, creation_height=None, creation_timestamp=None, activation_height=None, expiration_height=None, release_time=None, amount=None, support_amount=None, effective_amount=None, trending_score=None, trending_group=None, trending_mixed=None, trending_local=None, trending_global=None, reposted_claim_id=None, reposted=None, claim_type=None, stream_types=None, media_types=None, fee_currency=None, fee_amount=None, duration=None, any_tags=None, all_tags=None, not_tags=None, any_languages=None, all_languages=None, not_languages=None, any_locations=None, all_locations=None, not_locations=None, page=None, page_size=None, order_by=None, no_totals=None, wallet_id=None, include_purchase_receipt=None, include_is_my_output=None, remove_duplicates=None, has_source=None, sd_hash=None, has_no_source=None, new_sdk_server=None):
        """Search for stream and channel claims on the blockchain.

Arguments marked with "supports equality constraints" allow prepending the
value with an equality constraint such as '>', '>=', '<' and '<='
eg. --height=">400000" would limit results to only claims above 400k block height.

They also support multiple constraints passed as a list of the args described above.
eg. --release_time=[">1000000", "<2000000"]

        :param str name: claim name (normalized) (Optional)
        :param str text: full text search (Optional)
        :param str claim_id: full or partial claim id (Optional)
        :param list claim_ids: list of full claim ids (Optional)
        :param str txid: transaction id (Optional)
        :param str nout: position in the transaction (Optional)
        :param str channel: claims signed by this channel (argument is a URL which automatically gets resolved), see --channel_ids if you need to filter by multiple channels at the same time, includes claims with invalid signatures, use in conjunction with --valid_channel_signature (Optional)
        :param list channel_ids: claims signed by any of these channels (arguments must be claim ids of the channels), includes claims with invalid signatures, implies --has_channel_signature, use in conjunction with --valid_channel_signature (Optional)
        :param list not_channel_ids: exclude claims signed by any of these channels (arguments must be claim ids of the channels) (Optional)
        :param bool has_channel_signature: claims with a channel signature (valid or invalid) (Optional)
        :param bool valid_channel_signature: claims with a valid channel signature or no signature, use in conjunction with --has_channel_signature to only get claims with valid signatures (Optional)
        :param bool invalid_channel_signature: claims with invalid channel signature or no signature, use in conjunction with --has_channel_signature to only get claims with invalid signatures (Optional)
        :param int limit_claims_per_channel: only return up to the specified number of claims per channel (Optional)
        :param bool is_controlling: winning claims of their respective name (Optional)
        :param str public_key_id: only return channels having this public key id, this is the same key as used in the wallet file to map channel certificate private keys: {'public_key_id': 'private key'} (Optional)
        :param int height: last updated block height (supports equality constraints) (Optional)
        :param int timestamp: last updated timestamp (supports equality constraints) (Optional)
        :param int creation_height: created at block height (supports equality constraints) (Optional)
        :param int creation_timestamp: created at timestamp (supports equality constraints) (Optional)
        :param int activation_height: height at which claim starts competing for name (supports equality constraints) (Optional)
        :param int expiration_height: height at which claim will expire (supports equality constraints) (Optional)
        :param int release_time: limit to claims self-described as having been released to the public on or after this UTC timestamp, when claim does not provide a release time the publish time is used instead (supports equality constraints) (Optional)
        :param int amount: limit by claim value (supports equality constraints) (Optional)
        :param int support_amount: limit by supports and tips received (supports equality constraints) (Optional)
        :param int effective_amount: limit by total value (initial claim value plus all tips and supports received), this amount is blank until claim has reached activation height (supports equality constraints) (Optional)
        :param int trending_score: limit by trending score (supports equality constraints) (Optional)
        :param int trending_group: DEPRECATED - instead please use trending_score (Optional)
        :param int trending_mixed: DEPRECATED - instead please use trending_score (Optional)
        :param int trending_local: DEPRECATED - instead please use trending_score (Optional)
        :param int trending_global: DEPRECATED - instead please use trending_score (Optional)
        :param str reposted_claim_id: all reposts of the specified original claim id (Optional)
        :param int reposted: claims reposted this many times (supports equality constraints) (Optional)
        :param str claim_type: filter by 'channel', 'stream', 'repost' or 'collection' (Optional)
        :param list stream_types: filter by 'video', 'image', 'document', etc (Optional)
        :param list media_types: filter by 'video/mp4', 'image/png', etc (Optional)
        :param str fee_currency: specify fee currency: LBC, BTC, USD (Optional)
        :param float fee_amount: content download fee (supports equality constraints) (Optional)
        :param int duration: duration of video or audio in seconds (supports equality constraints) (Optional)
        :param list any_tags: find claims containing any of the tags (Optional)
        :param list all_tags: find claims containing every tag (Optional)
        :param list not_tags: find claims not containing any of these tags (Optional)
        :param list any_languages: find claims containing any of the languages (Optional)
        :param list all_languages: find claims containing every language (Optional)
        :param list not_languages: find claims not containing any of these languages (Optional)
        :param list any_locations: find claims containing any of the locations (Optional)
        :param list all_locations: find claims containing every location (Optional)
        :param list not_locations: find claims not containing any of these locations (Optional)
        :param int page: page to return during paginating (Optional)
        :param int page_size: number of items on page during pagination (Optional)
        :param list order_by: field to order by, default is descending order, to do an ascending order prepend ^ to the field name, eg. '^amount' available fields: 'name', 'height', 'release_time', 'publish_time', 'amount', 'effective_amount', 'support_amount', 'trending_group', 'trending_mixed', 'trending_local', 'trending_global', 'activation_height' (Optional)
        :param bool no_totals: do not calculate the total number of pages and items in result set (significant performance boost) (Optional)
        :param str wallet_id: wallet to check for claim purchase receipts (Optional)
        :param bool include_purchase_receipt: lookup and include a receipt if this wallet has purchased the claim (Optional)
        :param bool include_is_my_output: lookup and include a boolean indicating if claim being resolved is yours (Optional)
        :param bool remove_duplicates: removes duplicated content from search by picking either the original claim or the oldest matching repost (Optional)
        :param bool has_source: find claims containing a source field (Optional)
        :param str sd_hash: find claims where the source stream descriptor hash matches (partially or completely) the given hexadecimal string (Optional)
        :param bool has_no_source: find claims not containing a source field (Optional)
        :param str new_sdk_server: URL of the new SDK server (EXPERIMENTAL) (Optional)
        """
        __params_map = {'name': name,
                        'text': text,
                        'claim_id': claim_id,
                        'claim_ids': claim_ids,
                        'txid': txid,
                        'nout': nout,
                        'channel': channel,
                        'channel_ids': channel_ids,
                        'not_channel_ids': not_channel_ids,
                        'has_channel_signature': has_channel_signature,
                        'valid_channel_signature': valid_channel_signature,
                        'invalid_channel_signature': invalid_channel_signature,
                        'limit_claims_per_channel': limit_claims_per_channel,
                        'is_controlling': is_controlling,
                        'public_key_id': public_key_id,
                        'height': height,
                        'timestamp': timestamp,
                        'creation_height': creation_height,
                        'creation_timestamp': creation_timestamp,
                        'activation_height': activation_height,
                        'expiration_height': expiration_height,
                        'release_time': release_time,
                        'amount': amount,
                        'support_amount': support_amount,
                        'effective_amount': effective_amount,
                        'trending_score': trending_score,
                        'trending_group': trending_group,
                        'trending_mixed': trending_mixed,
                        'trending_local': trending_local,
                        'trending_global': trending_global,
                        'reposted_claim_id': reposted_claim_id,
                        'reposted': reposted,
                        'claim_type': claim_type,
                        'stream_types': stream_types,
                        'media_types': media_types,
                        'fee_currency': fee_currency,
                        'fee_amount': fee_amount,
                        'duration': duration,
                        'any_tags': any_tags,
                        'all_tags': all_tags,
                        'not_tags': not_tags,
                        'any_languages': any_languages,
                        'all_languages': all_languages,
                        'not_languages': not_languages,
                        'any_locations': any_locations,
                        'all_locations': all_locations,
                        'not_locations': not_locations,
                        'page': page,
                        'page_size': page_size,
                        'order_by': order_by,
                        'no_totals': no_totals,
                        'wallet_id': wallet_id,
                        'include_purchase_receipt': include_purchase_receipt,
                        'include_is_my_output': include_is_my_output,
                        'remove_duplicates': remove_duplicates,
                        'has_source': has_source,
                        'sd_hash': sd_hash,
                        'has_no_source': has_no_source,
                        'new_sdk_server': new_sdk_server}

        return self.make_request(SERVER_ADDRESS, 'claim_search', __params_map, timeout=self.timeout)

    def collection_abandon(self, claim_id=None, txid=None, nout=None, account_id=None, wallet_id=None, preview=None, blocking=None):
        """Abandon one of my collection claims.

        :param str claim_id: claim_id of the claim to abandon (Optional)
        :param str txid: txid of the claim to abandon (Optional)
        :param int nout: nout of the claim to abandon (Optional)
        :param str account_id: id of the account to use (Optional)
        :param str wallet_id: restrict operation to specific wallet (Optional)
        :param bool preview: do not broadcast the transaction (Optional)
        :param bool blocking: wait until abandon is in mempool (Optional)
        """
        __params_map = {'claim_id': claim_id,
                        'txid': txid,
                        'nout': nout,
                        'account_id': account_id,
                        'wallet_id': wallet_id,
                        'preview': preview,
                        'blocking': blocking}

        return self.make_request(SERVER_ADDRESS, 'collection_abandon', __params_map, timeout=self.timeout)

    def collection_create(self, name, bid, claims=None, allow_duplicate_name=None, title=None, description=None, tags=None, clear_languages=None, languages=None, locations=None, thumbnail_url=None, channel_id=None, channel_name=None, channel_account_id=None, account_id=None, wallet_id=None, funding_account_ids=None, claim_address=None, preview=None, blocking=None):
        """Create a new collection.

        :param str name: name of the collection
        :param float bid: amount to back the claim
        :param list claims: claim ids to be included in the collection (Optional)
        :param bool allow_duplicate_name: create new collection even if one already exists with given name. default: false. (Optional)
        :param str title: title of the collection (Optional)
        :param str description: description of the collection (Optional)
        :param list tags: content tags (Optional)
        :param bool clear_languages: clear existing languages (prior to adding new ones) (Optional)
        :param list languages: languages used by the collection, using RFC 5646 format, eg: for English `--languages=en` for Spanish (Spain) `--languages=es-ES` for Spanish (Mexican) `--languages=es-MX` for Chinese (Simplified) `--languages=zh-Hans` for Chinese (Traditional) `--languages=zh-Hant` (Optional)
        :param list locations: locations of the collection, consisting of 2 letter `country` code and a `state`, `city` and a postal `code` along with a `latitude` and `longitude`. for JSON RPC: pass a dictionary with aforementioned attributes as keys, eg: ... "locations": [{'country': 'US', 'state': 'NH'}] ... for command line: pass a colon delimited list with values in the following order: "COUNTRY:STATE:CITY:CODE:LATITUDE:LONGITUDE" making sure to include colon for blank values, for example to provide only the city: ... --locations="::Manchester" with all values set: ... --locations="US:NH:Manchester:03101:42.990605:-71.460989" optionally, you can just pass the "LATITUDE:LONGITUDE": ... --locations="42.990605:-71.460989" finally, you can also pass JSON string of dictionary on the command line as you would via JSON RPC ... --locations="{'country': 'US', 'state': 'NH'}" (Optional)
        :param str thumbnail_url: thumbnail url (Optional)
        :param str channel_id: claim id of the publisher channel (Optional)
        :param str channel_name: name of the publisher channel (Optional)
        :param str channel_account_id: one or more account ids for accounts to look in for channel certificates, defaults to all accounts. (Optional)
        :param str account_id: account to use for holding the transaction (Optional)
        :param str wallet_id: restrict operation to specific wallet (Optional)
        :param list funding_account_ids: ids of accounts to fund this transaction (Optional)
        :param str claim_address: address where the collection is sent to, if not specified it will be determined automatically from the account (Optional)
        :param bool preview: do not broadcast the transaction (Optional)
        :param bool blocking: wait until transaction is in mempool (Optional)
        """
        __params_map = {'name': name,
                        'bid': bid,
                        'claims': claims,
                        'allow_duplicate_name': allow_duplicate_name,
                        'title': title,
                        'description': description,
                        'tags': tags,
                        'clear_languages': clear_languages,
                        'languages': languages,
                        'locations': locations,
                        'thumbnail_url': thumbnail_url,
                        'channel_id': channel_id,
                        'channel_name': channel_name,
                        'channel_account_id': channel_account_id,
                        'account_id': account_id,
                        'wallet_id': wallet_id,
                        'funding_account_ids': funding_account_ids,
                        'claim_address': claim_address,
                        'preview': preview,
                        'blocking': blocking}

        return self.make_request(SERVER_ADDRESS, 'collection_create', __params_map, timeout=self.timeout)

    def collection_list(self, resolve=None, resolve_claims=None, account_id=None, wallet_id=None, page=None, page_size=None):
        """List my collection claims.

        :param bool resolve: resolve collection claim (Optional)
        :param int resolve_claims: resolve every claim (Optional)
        :param str account_id: id of the account to use (Optional)
        :param str wallet_id: restrict results to specific wallet (Optional)
        :param int page: page to return during paginating (Optional)
        :param int page_size: number of items on page during pagination (Optional)
        """
        __params_map = {'resolve': resolve,
                        'resolve_claims': resolve_claims,
                        'account_id': account_id,
                        'wallet_id': wallet_id,
                        'page': page,
                        'page_size': page_size}

        return self.make_request(SERVER_ADDRESS, 'collection_list', __params_map, timeout=self.timeout)

    def collection_resolve(self, claim_id=None, url=None, wallet_id=None, page=None, page_size=None):
        """Resolve claims in the collection.

        :param str claim_id: claim id of the collection (Optional)
        :param str url: url of the collection (Optional)
        :param str wallet_id: restrict results to specific wallet (Optional)
        :param int page: page to return during paginating (Optional)
        :param int page_size: number of items on page during pagination (Optional)
        """
        __params_map = {'claim_id': claim_id,
                        'url': url,
                        'wallet_id': wallet_id,
                        'page': page,
                        'page_size': page_size}

        return self.make_request(SERVER_ADDRESS, 'collection_resolve', __params_map, timeout=self.timeout)

    def collection_update(self, claim_id, bid=None, claims=None, clear_claims=None, title=None, description=None, tags=None, clear_tags=None, languages=None, clear_languages=None, locations=None, clear_locations=None, thumbnail_url=None, channel_id=None, channel_name=None, channel_account_id=None, account_id=None, wallet_id=None, funding_account_ids=None, claim_address=None, preview=None, blocking=None, replace=None):
        """Update an existing collection claim.

        :param str claim_id: claim_id of the collection to update
        :param float bid: amount to back the claim (Optional)
        :param list claims: claim ids (Optional)
        :param bool clear_claims: clear existing claim references (prior to adding new ones) (Optional)
        :param str title: title of the collection (Optional)
        :param str description: description of the collection (Optional)
        :param list tags: add content tags (Optional)
        :param bool clear_tags: clear existing tags (prior to adding new ones) (Optional)
        :param list languages: languages used by the collection, using RFC 5646 format, eg: for English `--languages=en` for Spanish (Spain) `--languages=es-ES` for Spanish (Mexican) `--languages=es-MX` for Chinese (Simplified) `--languages=zh-Hans` for Chinese (Traditional) `--languages=zh-Hant` (Optional)
        :param bool clear_languages: clear existing languages (prior to adding new ones) (Optional)
        :param list locations: locations of the collection, consisting of 2 letter `country` code and a `state`, `city` and a postal `code` along with a `latitude` and `longitude`. for JSON RPC: pass a dictionary with aforementioned attributes as keys, eg: ... "locations": [{'country': 'US', 'state': 'NH'}] ... for command line: pass a colon delimited list with values in the following order: "COUNTRY:STATE:CITY:CODE:LATITUDE:LONGITUDE" making sure to include colon for blank values, for example to provide only the city: ... --locations="::Manchester" with all values set: ... --locations="US:NH:Manchester:03101:42.990605:-71.460989" optionally, you can just pass the "LATITUDE:LONGITUDE": ... --locations="42.990605:-71.460989" finally, you can also pass JSON string of dictionary on the command line as you would via JSON RPC ... --locations="{'country': 'US', 'state': 'NH'}" (Optional)
        :param bool clear_locations: clear existing locations (prior to adding new ones) (Optional)
        :param str thumbnail_url: thumbnail url (Optional)
        :param str channel_id: claim id of the publisher channel (Optional)
        :param str channel_name: name of the publisher channel (Optional)
        :param str channel_account_id: one or more account ids for accounts to look in for channel certificates, defaults to all accounts. (Optional)
        :param str account_id: account in which to look for collection (default: all) (Optional)
        :param str wallet_id: restrict operation to specific wallet (Optional)
        :param list funding_account_ids: ids of accounts to fund this transaction (Optional)
        :param str claim_address: address where the collection is sent (Optional)
        :param bool preview: do not broadcast the transaction (Optional)
        :param bool blocking: wait until transaction is in mempool (Optional)
        :param bool replace: instead of modifying specific values on the collection, this will clear all existing values and only save passed in values, useful for form submissions where all values are always set (Optional)
        """
        __params_map = {'claim_id': claim_id,
                        'bid': bid,
                        'claims': claims,
                        'clear_claims': clear_claims,
                        'title': title,
                        'description': description,
                        'tags': tags,
                        'clear_tags': clear_tags,
                        'languages': languages,
                        'clear_languages': clear_languages,
                        'locations': locations,
                        'clear_locations': clear_locations,
                        'thumbnail_url': thumbnail_url,
                        'channel_id': channel_id,
                        'channel_name': channel_name,
                        'channel_account_id': channel_account_id,
                        'account_id': account_id,
                        'wallet_id': wallet_id,
                        'funding_account_ids': funding_account_ids,
                        'claim_address': claim_address,
                        'preview': preview,
                        'blocking': blocking,
                        'replace': replace}

        return self.make_request(SERVER_ADDRESS, 'collection_update', __params_map, timeout=self.timeout)

    def file_delete(self, delete_from_download_dir=None, delete_all=None, sd_hash=None, file_name=None, stream_hash=None, rowid=None, claim_id=None, txid=None, nout=None, claim_name=None, channel_claim_id=None, channel_name=None):
        """Delete a LBRY file

        :param bool delete_from_download_dir: delete file from download directory, instead of just deleting blobs (Optional)
        :param bool delete_all: if there are multiple matching files, allow the deletion of multiple files. Otherwise do not delete anything. (Optional)
        :param str sd_hash: delete by file sd hash (Optional)
        :param str file_name: delete by file name in downloads folder (Optional)
        :param str stream_hash: delete by file stream hash (Optional)
        :param int rowid: delete by file row id (Optional)
        :param str claim_id: delete by file claim id (Optional)
        :param str txid: delete by file claim txid (Optional)
        :param int nout: delete by file claim nout (Optional)
        :param str claim_name: delete by file claim name (Optional)
        :param str channel_claim_id: delete by file channel claim id (Optional)
        :param str channel_name: delete by file channel claim name (Optional)
        """
        __params_map = {'delete_from_download_dir': delete_from_download_dir,
                        'delete_all': delete_all,
                        'sd_hash': sd_hash,
                        'file_name': file_name,
                        'stream_hash': stream_hash,
                        'rowid': rowid,
                        'claim_id': claim_id,
                        'txid': txid,
                        'nout': nout,
                        'claim_name': claim_name,
                        'channel_claim_id': channel_claim_id,
                        'channel_name': channel_name}

        return self.make_request(SERVER_ADDRESS, 'file_delete', __params_map, timeout=self.timeout)

    def file_list(self, sd_hash=None, file_name=None, stream_hash=None, rowid=None, added_on=None, claim_id=None, outpoint=None, txid=None, nout=None, channel_claim_id=None, channel_name=None, claim_name=None, blobs_in_stream=None, download_path=None, uploading_to_reflector=None, is_fully_reflected=None, status=None, completed=None, blobs_remaining=None, sort=None, comparison=None, page=None, page_size=None, wallet_id=None):
        """List files limited by optional filters

        :param str sd_hash: get file with matching sd hash (Optional)
        :param str file_name: get file with matching file name in the downloads folder (Optional)
        :param str stream_hash: get file with matching stream hash (Optional)
        :param int rowid: get file with matching row id (Optional)
        :param int added_on: get file with matching time of insertion (Optional)
        :param str claim_id: get file with matching claim id(s) (Optional)
        :param str outpoint: get file with matching claim outpoint(s) (Optional)
        :param str txid: get file with matching claim txid (Optional)
        :param int nout: get file with matching claim nout (Optional)
        :param str channel_claim_id: get file with matching channel claim id(s) (Optional)
        :param str channel_name: get file with matching channel name (Optional)
        :param str claim_name: get file with matching claim name (Optional)
        :param int blobs_in_stream: get file with matching blobs in stream (Optional)
        :param str download_path: get file with matching download path (Optional)
        :param bool uploading_to_reflector: get files currently uploading to reflector (Optional)
        :param bool is_fully_reflected: get files that have been uploaded to reflector (Optional)
        :param str status: match by status, ( running | finished | stopped ) (Optional)
        :param bool completed: match only completed (Optional)
        :param int blobs_remaining: amount of remaining blobs to download (Optional)
        :param str sort: field to sort by (one of the above filter fields) (Optional)
        :param str comparison: logical comparison, (eq | ne | g | ge | l | le | in) (Optional)
        :param int page: page to return during paginating (Optional)
        :param int page_size: number of items on page during pagination (Optional)
        :param str wallet_id: add purchase receipts from this wallet (Optional)
        """
        __params_map = {'sd_hash': sd_hash,
                        'file_name': file_name,
                        'stream_hash': stream_hash,
                        'rowid': rowid,
                        'added_on': added_on,
                        'claim_id': claim_id,
                        'outpoint': outpoint,
                        'txid': txid,
                        'nout': nout,
                        'channel_claim_id': channel_claim_id,
                        'channel_name': channel_name,
                        'claim_name': claim_name,
                        'blobs_in_stream': blobs_in_stream,
                        'download_path': download_path,
                        'uploading_to_reflector': uploading_to_reflector,
                        'is_fully_reflected': is_fully_reflected,
                        'status': status,
                        'completed': completed,
                        'blobs_remaining': blobs_remaining,
                        'sort': sort,
                        'comparison': comparison,
                        'page': page,
                        'page_size': page_size,
                        'wallet_id': wallet_id}

        return self.make_request(SERVER_ADDRESS, 'file_list', __params_map, timeout=self.timeout)

    def file_reflect(self, sd_hash=None, file_name=None, stream_hash=None, rowid=None, reflector=None):
        """Reflect all the blobs in a file matching the filter criteria

        :param str sd_hash: get file with matching sd hash (Optional)
        :param str file_name: get file with matching file name in the downloads folder (Optional)
        :param str stream_hash: get file with matching stream hash (Optional)
        :param int rowid: get file with matching row id (Optional)
        :param str reflector: reflector server, ip address or url by default choose a server from the config (Optional)
        """
        __params_map = {'sd_hash': sd_hash,
                        'file_name': file_name,
                        'stream_hash': stream_hash,
                        'rowid': rowid,
                        'reflector': reflector}

        return self.make_request(SERVER_ADDRESS, 'file_reflect', __params_map, timeout=self.timeout)

    def file_save(self, file_name=None, download_directory=None, sd_hash=None, stream_hash=None, rowid=None, claim_id=None, txid=None, nout=None, claim_name=None, channel_claim_id=None, channel_name=None):
        """Start saving a file to disk.

        :param str file_name: file name to save to (Optional)
        :param str download_directory: directory to save into (Optional)
        :param str sd_hash: save file with matching sd hash (Optional)
        :param str stream_hash: save file with matching stream hash (Optional)
        :param int rowid: save file with matching row id (Optional)
        :param str claim_id: save file with matching claim id (Optional)
        :param str txid: save file with matching claim txid (Optional)
        :param int nout: save file with matching claim nout (Optional)
        :param str claim_name: save file with matching claim name (Optional)
        :param str channel_claim_id: save file with matching channel claim id (Optional)
        :param str channel_name: save file with matching channel claim name (Optional)
        """
        __params_map = {'file_name': file_name,
                        'download_directory': download_directory,
                        'sd_hash': sd_hash,
                        'stream_hash': stream_hash,
                        'rowid': rowid,
                        'claim_id': claim_id,
                        'txid': txid,
                        'nout': nout,
                        'claim_name': claim_name,
                        'channel_claim_id': channel_claim_id,
                        'channel_name': channel_name}

        return self.make_request(SERVER_ADDRESS, 'file_save', __params_map, timeout=self.timeout)

    def file_set_status(self, status, sd_hash=None, file_name=None, stream_hash=None, rowid=None):
        """Start or stop downloading a file

        :param str status: one of "start" or "stop"
        :param str sd_hash: set status of file with matching sd hash (Optional)
        :param str file_name: set status of file with matching file name in the downloads folder (Optional)
        :param str stream_hash: set status of file with matching stream hash (Optional)
        :param int rowid: set status of file with matching row id (Optional)
        """
        __params_map = {'status': status,
                        'sd_hash': sd_hash,
                        'file_name': file_name,
                        'stream_hash': stream_hash,
                        'rowid': rowid}

        return self.make_request(SERVER_ADDRESS, 'file_set_status', __params_map, timeout=self.timeout)

    def peer_list(self, blob_hash, page=None, page_size=None):
        """Get peers for blob hash

        :param str blob_hash: find available peers for this blob hash
        :param int page: page to return during paginating (Optional)
        :param int page_size: number of items on page during pagination (Optional)
        """
        __params_map = {'blob_hash': blob_hash,
                        'page': page,
                        'page_size': page_size}

        return self.make_request(SERVER_ADDRESS, 'peer_list', __params_map, timeout=self.timeout)

    def peer_ping(self):
        """Send a kademlia ping to the specified peer. If address and port are provided the peer is directly pinged,
if not provided the peer is located first.

        """
        __params_map = {}

        return self.make_request(SERVER_ADDRESS, 'peer_ping', __params_map, timeout=self.timeout)

    def preference_get(self, key=None, wallet_id=None):
        """Get preference value for key or all values if not key is passed in.

        :param str key: key associated with value (Optional)
        :param str wallet_id: restrict operation to specific wallet (Optional)
        """
        __params_map = {'key': key,
                        'wallet_id': wallet_id}

        return self.make_request(SERVER_ADDRESS, 'preference_get', __params_map, timeout=self.timeout)

    def preference_set(self, key, value, wallet_id=None):
        """Set preferences

        :param str key: key associated with value
        :param str value: key associated with value
        :param str wallet_id: restrict operation to specific wallet (Optional)
        """
        __params_map = {'key': key,
                        'value': value,
                        'wallet_id': wallet_id}

        return self.make_request(SERVER_ADDRESS, 'preference_set', __params_map, timeout=self.timeout)

    def purchase_create(self, claim_id=None, url=None, wallet_id=None, funding_account_ids=None, allow_duplicate_purchase=None, override_max_key_fee=None, preview=None, blocking=None):
        """Purchase a claim.

        :param str claim_id: claim id of claim to purchase (Optional)
        :param str url: lookup claim to purchase by url (Optional)
        :param str wallet_id: restrict operation to specific wallet (Optional)
        :param list funding_account_ids: ids of accounts to fund this transaction (Optional)
        :param bool allow_duplicate_purchase: allow purchasing claim_id you already own (Optional)
        :param bool override_max_key_fee: ignore max key fee for this purchase (Optional)
        :param bool preview: do not broadcast the transaction (Optional)
        :param bool blocking: wait until transaction is in mempool (Optional)
        """
        __params_map = {'claim_id': claim_id,
                        'url': url,
                        'wallet_id': wallet_id,
                        'funding_account_ids': funding_account_ids,
                        'allow_duplicate_purchase': allow_duplicate_purchase,
                        'override_max_key_fee': override_max_key_fee,
                        'preview': preview,
                        'blocking': blocking}

        return self.make_request(SERVER_ADDRESS, 'purchase_create', __params_map, timeout=self.timeout)

    def purchase_list(self, claim_id=None, resolve=None, account_id=None, wallet_id=None, page=None, page_size=None):
        """List my claim purchases.

        :param str claim_id: purchases for specific claim (Optional)
        :param str resolve: include resolved claim information (Optional)
        :param str account_id: id of the account to query (Optional)
        :param str wallet_id: restrict results to specific wallet (Optional)
        :param int page: page to return during paginating (Optional)
        :param int page_size: number of items on page during pagination (Optional)
        """
        __params_map = {'claim_id': claim_id,
                        'resolve': resolve,
                        'account_id': account_id,
                        'wallet_id': wallet_id,
                        'page': page,
                        'page_size': page_size}

        return self.make_request(SERVER_ADDRESS, 'purchase_list', __params_map, timeout=self.timeout)

    def settings_clear(self):
        """Clear daemon settings

        """
        __params_map = {}

        return self.make_request(SERVER_ADDRESS, 'settings_clear', __params_map, timeout=self.timeout)

    def settings_get(self):
        """Get daemon settings

        """
        __params_map = {}

        return self.make_request(SERVER_ADDRESS, 'settings_get', __params_map, timeout=self.timeout)

    def settings_set(self):
        """Set daemon settings

        """
        __params_map = {}

        return self.make_request(SERVER_ADDRESS, 'settings_set', __params_map, timeout=self.timeout)

    def stream_abandon(self, claim_id=None, txid=None, nout=None, account_id=None, wallet_id=None, preview=None, blocking=None):
        """Abandon one of my stream claims.

        :param str claim_id: claim_id of the claim to abandon (Optional)
        :param str txid: txid of the claim to abandon (Optional)
        :param int nout: nout of the claim to abandon (Optional)
        :param str account_id: id of the account to use (Optional)
        :param str wallet_id: restrict operation to specific wallet (Optional)
        :param bool preview: do not broadcast the transaction (Optional)
        :param bool blocking: wait until abandon is in mempool (Optional)
        """
        __params_map = {'claim_id': claim_id,
                        'txid': txid,
                        'nout': nout,
                        'account_id': account_id,
                        'wallet_id': wallet_id,
                        'preview': preview,
                        'blocking': blocking}

        return self.make_request(SERVER_ADDRESS, 'stream_abandon', __params_map, timeout=self.timeout)

    def stream_cost_estimate(self, uri):
        """Get estimated cost for a lbry stream

        :param str uri: uri to use
        """
        __params_map = {'uri': uri}

        return self.make_request(SERVER_ADDRESS, 'stream_cost_estimate', __params_map, timeout=self.timeout)

    def stream_create(self, name, bid, file_path=None, file_name=None, file_hash=None, validate_file=None, optimize_file=None, allow_duplicate_name=None, fee_currency=None, fee_amount=None, fee_address=None, title=None, description=None, author=None, tags=None, languages=None, locations=None, license=None, license_url=None, thumbnail_url=None, release_time=None, width=None, height=None, duration=None, sd_hash=None, channel_id=None, channel_name=None, channel_account_id=None, account_id=None, wallet_id=None, funding_account_ids=None, claim_address=None, preview=None, blocking=None):
        """Make a new stream claim and announce the associated file to lbrynet.

        :param str name: name of the content (can only consist of a-z A-Z 0-9 and -(dash))
        :param float bid: amount to back the claim
        :param str file_path: path to file to be associated with name. (Optional)
        :param str file_name: name of file to be associated with stream. (Optional)
        :param str file_hash: hash of file to be associated with stream. (Optional)
        :param bool validate_file: validate that the video container and encodings match common web browser support or that optimization succeeds if specified. FFmpeg is required (Optional)
        :param bool optimize_file: transcode the video & audio if necessary to ensure common web browser support. FFmpeg is required (Optional)
        :param bool allow_duplicate_name: create new claim even if one already exists with given name. default: false. (Optional)
        :param str fee_currency: specify fee currency (Optional)
        :param float fee_amount: content download fee (Optional)
        :param str fee_address: address where to send fee payments, will use value from --claim_address if not provided (Optional)
        :param str title: title of the publication (Optional)
        :param str description: description of the publication (Optional)
        :param str author: author of the publication. The usage for this field is not the same as for channels. The author field is used to credit an author who is not the publisher and is not represented by the channel. For example, a pdf file of 'The Odyssey' has an author of 'Homer' but may by published to a channel such as '@classics', or to no channel at all (Optional)
        :param list tags: add content tags (Optional)
        :param list languages: languages used by the channel, using RFC 5646 format, eg: for English `--languages=en` for Spanish (Spain) `--languages=es-ES` for Spanish (Mexican) `--languages=es-MX` for Chinese (Simplified) `--languages=zh-Hans` for Chinese (Traditional) `--languages=zh-Hant` (Optional)
        :param list locations: locations relevant to the stream, consisting of 2 letter `country` code and a `state`, `city` and a postal `code` along with a `latitude` and `longitude`. for JSON RPC: pass a dictionary with aforementioned attributes as keys, eg: ... "locations": [{'country': 'US', 'state': 'NH'}] ... for command line: pass a colon delimited list with values in the following order: "COUNTRY:STATE:CITY:CODE:LATITUDE:LONGITUDE" making sure to include colon for blank values, for example to provide only the city: ... --locations="::Manchester" with all values set: ... --locations="US:NH:Manchester:03101:42.990605:-71.460989" optionally, you can just pass the "LATITUDE:LONGITUDE": ... --locations="42.990605:-71.460989" finally, you can also pass JSON string of dictionary on the command line as you would via JSON RPC ... --locations="{'country': 'US', 'state': 'NH'}" (Optional)
        :param str license: publication license (Optional)
        :param str license_url: publication license url (Optional)
        :param str thumbnail_url: thumbnail url (Optional)
        :param int release_time: original public release of content, seconds since UNIX epoch (Optional)
        :param int width: image/video width, automatically calculated from media file (Optional)
        :param int height: image/video height, automatically calculated from media file (Optional)
        :param int duration: audio/video duration in seconds, automatically calculated (Optional)
        :param str sd_hash: sd_hash of stream (Optional)
        :param str channel_id: claim id of the publisher channel (Optional)
        :param str channel_name: name of the publisher channel (Optional)
        :param str channel_account_id: one or more account ids for accounts to look in for channel certificates, defaults to all accounts. (Optional)
        :param str account_id: account to use for holding the transaction (Optional)
        :param str wallet_id: restrict operation to specific wallet (Optional)
        :param list funding_account_ids: ids of accounts to fund this transaction (Optional)
        :param str claim_address: address where the claim is sent to, if not specified it will be determined automatically from the account (Optional)
        :param bool preview: do not broadcast the transaction (Optional)
        :param bool blocking: wait until transaction is in mempool (Optional)
        """
        __params_map = {'name': name,
                        'bid': bid,
                        'file_path': file_path,
                        'file_name': file_name,
                        'file_hash': file_hash,
                        'validate_file': validate_file,
                        'optimize_file': optimize_file,
                        'allow_duplicate_name': allow_duplicate_name,
                        'fee_currency': fee_currency,
                        'fee_amount': fee_amount,
                        'fee_address': fee_address,
                        'title': title,
                        'description': description,
                        'author': author,
                        'tags': tags,
                        'languages': languages,
                        'locations': locations,
                        'license': license,
                        'license_url': license_url,
                        'thumbnail_url': thumbnail_url,
                        'release_time': release_time,
                        'width': width,
                        'height': height,
                        'duration': duration,
                        'sd_hash': sd_hash,
                        'channel_id': channel_id,
                        'channel_name': channel_name,
                        'channel_account_id': channel_account_id,
                        'account_id': account_id,
                        'wallet_id': wallet_id,
                        'funding_account_ids': funding_account_ids,
                        'claim_address': claim_address,
                        'preview': preview,
                        'blocking': blocking}

        return self.make_request(SERVER_ADDRESS, 'stream_create', __params_map, timeout=self.timeout)

    def stream_list(self, name=None, claim_id=None, is_spent=None, account_id=None, wallet_id=None, page=None, page_size=None, resolve=None, no_totals=None):
        """List my stream claims.

        :param list name: stream name (Optional)
        :param list claim_id: stream id (Optional)
        :param bool is_spent: shows previous stream updates and abandons (Optional)
        :param str account_id: id of the account to query (Optional)
        :param str wallet_id: restrict results to specific wallet (Optional)
        :param int page: page to return during paginating (Optional)
        :param int page_size: number of items on page during pagination (Optional)
        :param bool resolve: resolves each stream to provide additional metadata (Optional)
        :param bool no_totals: do not calculate the total number of pages and items in result set (significant performance boost) (Optional)
        """
        __params_map = {'name': name,
                        'claim_id': claim_id,
                        'is_spent': is_spent,
                        'account_id': account_id,
                        'wallet_id': wallet_id,
                        'page': page,
                        'page_size': page_size,
                        'resolve': resolve,
                        'no_totals': no_totals}

        return self.make_request(SERVER_ADDRESS, 'stream_list', __params_map, timeout=self.timeout)

    def stream_repost(self, name, bid, claim_id, allow_duplicate_name=None, title=None, description=None, tags=None, channel_id=None, channel_name=None, channel_account_id=None, account_id=None, wallet_id=None, funding_account_ids=None, claim_address=None, preview=None, blocking=None):
        """Creates a claim that references an existing stream by its claim id.

        :param str name: name of the content (can only consist of a-z A-Z 0-9 and -(dash))
        :param float bid: amount to back the claim
        :param str claim_id: id of the claim being reposted
        :param bool allow_duplicate_name: create new claim even if one already exists with given name. default: false. (Optional)
        :param str title: title of the repost (Optional)
        :param str description: description of the repost (Optional)
        :param list tags: add repost tags (Optional)
        :param str channel_id: claim id of the publisher channel (Optional)
        :param str channel_name: name of the publisher channel (Optional)
        :param str channel_account_id: one or more account ids for accounts to look in for channel certificates, defaults to all accounts. (Optional)
        :param str account_id: account to use for holding the transaction (Optional)
        :param str wallet_id: restrict operation to specific wallet (Optional)
        :param list funding_account_ids: ids of accounts to fund this transaction (Optional)
        :param str claim_address: address where the claim is sent to, if not specified it will be determined automatically from the account (Optional)
        :param bool preview: do not broadcast the transaction (Optional)
        :param bool blocking: wait until transaction is in mempool (Optional)
        """
        __params_map = {'name': name,
                        'bid': bid,
                        'claim_id': claim_id,
                        'allow_duplicate_name': allow_duplicate_name,
                        'title': title,
                        'description': description,
                        'tags': tags,
                        'channel_id': channel_id,
                        'channel_name': channel_name,
                        'channel_account_id': channel_account_id,
                        'account_id': account_id,
                        'wallet_id': wallet_id,
                        'funding_account_ids': funding_account_ids,
                        'claim_address': claim_address,
                        'preview': preview,
                        'blocking': blocking}

        return self.make_request(SERVER_ADDRESS, 'stream_repost', __params_map, timeout=self.timeout)

    def stream_update(self, claim_id, bid=None, file_path=None, validate_file=None, optimize_file=None, file_name=None, file_size=None, file_hash=None, fee_currency=None, fee_amount=None, fee_address=None, clear_fee=None, title=None, description=None, author=None, tags=None, clear_tags=None, languages=None, clear_languages=None, locations=None, clear_locations=None, license=None, license_url=None, thumbnail_url=None, release_time=None, width=None, height=None, duration=None, sd_hash=None, channel_id=None, channel_name=None, clear_channel=None, channel_account_id=None, account_id=None, wallet_id=None, funding_account_ids=None, claim_address=None, preview=None, blocking=None, replace=None):
        """Update an existing stream claim and if a new file is provided announce it to lbrynet.

        :param str claim_id: id of the stream claim to update
        :param float bid: amount to back the claim (Optional)
        :param str file_path: path to file to be associated with name. (Optional)
        :param bool validate_file: validate that the video container and encodings match common web browser support or that optimization succeeds if specified. FFmpeg is required and file_path must be specified. (Optional)
        :param bool optimize_file: transcode the video & audio if necessary to ensure common web browser support. FFmpeg is required and file_path must be specified. (Optional)
        :param str file_name: override file name, defaults to name from file_path. (Optional)
        :param str file_size: override file size, otherwise automatically computed. (Optional)
        :param str file_hash: override file hash, otherwise automatically computed. (Optional)
        :param str fee_currency: specify fee currency (Optional)
        :param float fee_amount: content download fee (Optional)
        :param str fee_address: address where to send fee payments, will use value from --claim_address if not provided (Optional)
        :param bool clear_fee: clear previously set fee (Optional)
        :param str title: title of the publication (Optional)
        :param str description: description of the publication (Optional)
        :param str author: author of the publication. The usage for this field is not the same as for channels. The author field is used to credit an author who is not the publisher and is not represented by the channel. For example, a pdf file of 'The Odyssey' has an author of 'Homer' but may by published to a channel such as '@classics', or to no channel at all (Optional)
        :param list tags: add content tags (Optional)
        :param bool clear_tags: clear existing tags (prior to adding new ones) (Optional)
        :param list languages: languages used by the channel, using RFC 5646 format, eg: for English `--languages=en` for Spanish (Spain) `--languages=es-ES` for Spanish (Mexican) `--languages=es-MX` for Chinese (Simplified) `--languages=zh-Hans` for Chinese (Traditional) `--languages=zh-Hant` (Optional)
        :param bool clear_languages: clear existing languages (prior to adding new ones) (Optional)
        :param list locations: locations relevant to the stream, consisting of 2 letter `country` code and a `state`, `city` and a postal `code` along with a `latitude` and `longitude`. for JSON RPC: pass a dictionary with aforementioned attributes as keys, eg: ... "locations": [{'country': 'US', 'state': 'NH'}] ... for command line: pass a colon delimited list with values in the following order: "COUNTRY:STATE:CITY:CODE:LATITUDE:LONGITUDE" making sure to include colon for blank values, for example to provide only the city: ... --locations="::Manchester" with all values set: ... --locations="US:NH:Manchester:03101:42.990605:-71.460989" optionally, you can just pass the "LATITUDE:LONGITUDE": ... --locations="42.990605:-71.460989" finally, you can also pass JSON string of dictionary on the command line as you would via JSON RPC ... --locations="{'country': 'US', 'state': 'NH'}" (Optional)
        :param bool clear_locations: clear existing locations (prior to adding new ones) (Optional)
        :param str license: publication license (Optional)
        :param str license_url: publication license url (Optional)
        :param str thumbnail_url: thumbnail url (Optional)
        :param int release_time: original public release of content, seconds since UNIX epoch (Optional)
        :param int width: image/video width, automatically calculated from media file (Optional)
        :param int height: image/video height, automatically calculated from media file (Optional)
        :param int duration: audio/video duration in seconds, automatically calculated (Optional)
        :param str sd_hash: sd_hash of stream (Optional)
        :param str channel_id: claim id of the publisher channel (Optional)
        :param str channel_name: name of the publisher channel (Optional)
        :param bool clear_channel: remove channel signature (Optional)
        :param str channel_account_id: one or more account ids for accounts to look in for channel certificates, defaults to all accounts. (Optional)
        :param str account_id: account in which to look for stream (default: all) (Optional)
        :param str wallet_id: restrict operation to specific wallet (Optional)
        :param list funding_account_ids: ids of accounts to fund this transaction (Optional)
        :param str claim_address: address where the claim is sent to, if not specified it will be determined automatically from the account (Optional)
        :param bool preview: do not broadcast the transaction (Optional)
        :param bool blocking: wait until transaction is in mempool (Optional)
        :param bool replace: instead of modifying specific values on the stream, this will clear all existing values and only save passed in values, useful for form submissions where all values are always set (Optional)
        """
        __params_map = {'claim_id': claim_id,
                        'bid': bid,
                        'file_path': file_path,
                        'validate_file': validate_file,
                        'optimize_file': optimize_file,
                        'file_name': file_name,
                        'file_size': file_size,
                        'file_hash': file_hash,
                        'fee_currency': fee_currency,
                        'fee_amount': fee_amount,
                        'fee_address': fee_address,
                        'clear_fee': clear_fee,
                        'title': title,
                        'description': description,
                        'author': author,
                        'tags': tags,
                        'clear_tags': clear_tags,
                        'languages': languages,
                        'clear_languages': clear_languages,
                        'locations': locations,
                        'clear_locations': clear_locations,
                        'license': license,
                        'license_url': license_url,
                        'thumbnail_url': thumbnail_url,
                        'release_time': release_time,
                        'width': width,
                        'height': height,
                        'duration': duration,
                        'sd_hash': sd_hash,
                        'channel_id': channel_id,
                        'channel_name': channel_name,
                        'clear_channel': clear_channel,
                        'channel_account_id': channel_account_id,
                        'account_id': account_id,
                        'wallet_id': wallet_id,
                        'funding_account_ids': funding_account_ids,
                        'claim_address': claim_address,
                        'preview': preview,
                        'blocking': blocking,
                        'replace': replace}

        return self.make_request(SERVER_ADDRESS, 'stream_update', __params_map, timeout=self.timeout)

    def support_abandon(self, claim_id=None, txid=None, nout=None, keep=None, account_id=None, wallet_id=None, preview=None, blocking=None):
        """Abandon supports, including tips, of a specific claim, optionally
keeping some amount as supports.

        :param str claim_id: claim_id of the support to abandon (Optional)
        :param str txid: txid of the claim to abandon (Optional)
        :param int nout: nout of the claim to abandon (Optional)
        :param float keep: amount of lbc to keep as support (Optional)
        :param str account_id: id of the account to use (Optional)
        :param str wallet_id: restrict operation to specific wallet (Optional)
        :param bool preview: do not broadcast the transaction (Optional)
        :param bool blocking: wait until abandon is in mempool (Optional)
        """
        __params_map = {'claim_id': claim_id,
                        'txid': txid,
                        'nout': nout,
                        'keep': keep,
                        'account_id': account_id,
                        'wallet_id': wallet_id,
                        'preview': preview,
                        'blocking': blocking}

        return self.make_request(SERVER_ADDRESS, 'support_abandon', __params_map, timeout=self.timeout)

    def support_create(self, claim_id, amount, tip=None, channel_id=None, channel_name=None, channel_account_id=None, account_id=None, wallet_id=None, funding_account_ids=None, comment=None, preview=None, blocking=None):
        """Create a support or a tip for name claim.

        :param str claim_id: claim_id of the claim to support
        :param float amount: amount of support
        :param bool tip: send support to claim owner, default: false. (Optional)
        :param str channel_id: claim id of the supporters identity channel (Optional)
        :param str channel_name: name of the supporters identity channel (Optional)
        :param str channel_account_id: one or more account ids for accounts to look in for channel certificates, defaults to all accounts. (Optional)
        :param str account_id: account to use for holding the transaction (Optional)
        :param str wallet_id: restrict operation to specific wallet (Optional)
        :param list funding_account_ids: ids of accounts to fund this transaction (Optional)
        :param str comment: add a comment to the support (Optional)
        :param bool preview: do not broadcast the transaction (Optional)
        :param bool blocking: wait until transaction is in mempool (Optional)
        """
        __params_map = {'claim_id': claim_id,
                        'amount': amount,
                        'tip': tip,
                        'channel_id': channel_id,
                        'channel_name': channel_name,
                        'channel_account_id': channel_account_id,
                        'account_id': account_id,
                        'wallet_id': wallet_id,
                        'funding_account_ids': funding_account_ids,
                        'comment': comment,
                        'preview': preview,
                        'blocking': blocking}

        return self.make_request(SERVER_ADDRESS, 'support_create', __params_map, timeout=self.timeout)

    def support_list(self, name=None, claim_id=None, received=None, sent=None, staked=None, is_spent=None, account_id=None, wallet_id=None, page=None, page_size=None, no_totals=None):
        """List staked supports and sent/received tips.

        :param list name: claim name (Optional)
        :param list claim_id: claim id (Optional)
        :param bool received: only show received (tips) (Optional)
        :param bool sent: only show sent (tips) (Optional)
        :param bool staked: only show my staked supports (Optional)
        :param bool is_spent: show abandoned supports (Optional)
        :param str account_id: id of the account to query (Optional)
        :param str wallet_id: restrict results to specific wallet (Optional)
        :param int page: page to return during paginating (Optional)
        :param int page_size: number of items on page during pagination (Optional)
        :param bool no_totals: do not calculate the total number of pages and items in result set (significant performance boost) (Optional)
        """
        __params_map = {'name': name,
                        'claim_id': claim_id,
                        'received': received,
                        'sent': sent,
                        'staked': staked,
                        'is_spent': is_spent,
                        'account_id': account_id,
                        'wallet_id': wallet_id,
                        'page': page,
                        'page_size': page_size,
                        'no_totals': no_totals}

        return self.make_request(SERVER_ADDRESS, 'support_list', __params_map, timeout=self.timeout)

    def support_sum(self, claim_id=None, new_sdk_server=None, include_channel_content=None, page=None, page_size=None):
        """List total staked supports for a claim, grouped by the channel that signed the support.

If claim_id is a channel claim, you can use --include_channel_content to also include supports for
content claims in the channel.

!!!! NOTE: PAGINATION DOES NOT DO ANYTHING AT THE MOMENT !!!!!

        :param str claim_id: claim id (Optional)
        :param str new_sdk_server: URL of the new SDK server (EXPERIMENTAL) (Optional)
        :param bool include_channel_content: if claim_id is for a channel, include supports for claims in that channel (Optional)
        :param int page: page to return during paginating (Optional)
        :param int page_size: number of items on page during pagination (Optional)
        """
        __params_map = {'claim_id': claim_id,
                        'new_sdk_server': new_sdk_server,
                        'include_channel_content': include_channel_content,
                        'page': page,
                        'page_size': page_size}

        return self.make_request(SERVER_ADDRESS, 'support_sum', __params_map, timeout=self.timeout)

    def sync_apply(self, password=None, data=None, wallet_id=None, blocking=None):
        """Apply incoming synchronization data, if provided, and return a sync hash and update wallet data.

Wallet must be unlocked to perform this operation.

If "encrypt-on-disk" preference is True and supplied password is different from local password,
or there is no local password (because local wallet was not encrypted), then the supplied password
will be used for local encryption (overwriting previous local encryption password).

        :param str password: password to decrypt incoming and encrypt outgoing data (Optional)
        :param str data: incoming sync data, if any (Optional)
        :param str wallet_id: wallet being sync'ed (Optional)
        :param bool blocking: wait until any new accounts have sync'ed (Optional)
        """
        __params_map = {'password': password,
                        'data': data,
                        'wallet_id': wallet_id,
                        'blocking': blocking}

        return self.make_request(SERVER_ADDRESS, 'sync_apply', __params_map, timeout=self.timeout)

    def sync_hash(self, wallet_id=None):
        """Deterministic hash of the wallet.

        :param str wallet_id: wallet for which to generate hash (Optional)
        """
        __params_map = {'wallet_id': wallet_id}

        return self.make_request(SERVER_ADDRESS, 'sync_hash', __params_map, timeout=self.timeout)

    def tracemalloc_disable(self):
        """Disable tracemalloc memory tracing

        """
        __params_map = {}

        return self.make_request(SERVER_ADDRESS, 'tracemalloc_disable', __params_map, timeout=self.timeout)

    def tracemalloc_enable(self):
        """Enable tracemalloc memory tracing

        """
        __params_map = {}

        return self.make_request(SERVER_ADDRESS, 'tracemalloc_enable', __params_map, timeout=self.timeout)

    def tracemalloc_top(self, items):
        """Show most common objects, the place that created them and their size.

        :param int items: maximum items to return, from the most common
        """
        __params_map = {'items': items}

        return self.make_request(SERVER_ADDRESS, 'tracemalloc_top', __params_map, timeout=self.timeout)

    def transaction_list(self, account_id=None, wallet_id=None, page=None, page_size=None):
        """List transactions belonging to wallet

        :param str account_id: id of the account to query (Optional)
        :param str wallet_id: restrict results to specific wallet (Optional)
        :param int page: page to return during paginating (Optional)
        :param int page_size: number of items on page during pagination (Optional)
        """
        __params_map = {'account_id': account_id,
                        'wallet_id': wallet_id,
                        'page': page,
                        'page_size': page_size}

        return self.make_request(SERVER_ADDRESS, 'transaction_list', __params_map, timeout=self.timeout)

    def transaction_show(self, txid):
        """Get a decoded transaction from a txid

        :param str txid: txid of the transaction
        """
        __params_map = {'txid': txid}

        return self.make_request(SERVER_ADDRESS, 'transaction_show', __params_map, timeout=self.timeout)

    def txo_list(self, type=None, txid=None, claim_id=None, channel_id=None, not_channel_id=None, name=None, is_spent=None, is_not_spent=None, is_my_input_or_output=None, is_my_output=None, is_not_my_output=None, is_my_input=None, is_not_my_input=None, exclude_internal_transfers=None, include_received_tips=None, account_id=None, wallet_id=None, page=None, page_size=None, resolve=None, order_by=None, no_totals=None):
        """List my transaction outputs.

        :param list type: claim type: stream, channel, support, purchase, collection, repost, other (Optional)
        :param list txid: transaction id of outputs (Optional)
        :param list claim_id: claim id (Optional)
        :param list channel_id: claims in this channel (Optional)
        :param list not_channel_id: claims not in this channel (Optional)
        :param list name: claim name (Optional)
        :param bool is_spent: only show spent txos (Optional)
        :param bool is_not_spent: only show not spent txos (Optional)
        :param bool is_my_input_or_output: txos which have your inputs or your outputs, if using this flag the other related flags are ignored (--is_my_output, --is_my_input, etc) (Optional)
        :param bool is_my_output: show outputs controlled by you (Optional)
        :param bool is_not_my_output: show outputs not controlled by you (Optional)
        :param bool is_my_input: show outputs created by you (Optional)
        :param bool is_not_my_input: show outputs not created by you (Optional)
        :param bool exclude_internal_transfers: excludes any outputs that are exactly this combination: "--is_my_input --is_my_output --type=other" this allows to exclude "change" payments, this flag can be used in combination with any of the other flags (Optional)
        :param bool include_received_tips: calculate the amount of tips received for claim outputs (Optional)
        :param str account_id: id of the account to query (Optional)
        :param str wallet_id: restrict results to specific wallet (Optional)
        :param int page: page to return during paginating (Optional)
        :param int page_size: number of items on page during pagination (Optional)
        :param bool resolve: resolves each claim to provide additional metadata (Optional)
        :param str order_by: field to order by: 'name', 'height', 'amount' and 'none' (Optional)
        :param bool no_totals: do not calculate the total number of pages and items in result set (significant performance boost) (Optional)
        """
        __params_map = {'type': type,
                        'txid': txid,
                        'claim_id': claim_id,
                        'channel_id': channel_id,
                        'not_channel_id': not_channel_id,
                        'name': name,
                        'is_spent': is_spent,
                        'is_not_spent': is_not_spent,
                        'is_my_input_or_output': is_my_input_or_output,
                        'is_my_output': is_my_output,
                        'is_not_my_output': is_not_my_output,
                        'is_my_input': is_my_input,
                        'is_not_my_input': is_not_my_input,
                        'exclude_internal_transfers': exclude_internal_transfers,
                        'include_received_tips': include_received_tips,
                        'account_id': account_id,
                        'wallet_id': wallet_id,
                        'page': page,
                        'page_size': page_size,
                        'resolve': resolve,
                        'order_by': order_by,
                        'no_totals': no_totals}

        return self.make_request(SERVER_ADDRESS, 'txo_list', __params_map, timeout=self.timeout)

    def txo_plot(self, type=None, txid=None, claim_id=None, name=None, channel_id=None, not_channel_id=None, is_spent=None, is_not_spent=None, is_my_input_or_output=None, is_my_output=None, is_not_my_output=None, is_my_input=None, is_not_my_input=None, exclude_internal_transfers=None, account_id=None, wallet_id=None, days_back=None, start_day=None, days_after=None, end_day=None):
        """Plot transaction output sum over days.

        :param list type: claim type: stream, channel, support, purchase, collection, repost, other (Optional)
        :param list txid: transaction id of outputs (Optional)
        :param list claim_id: claim id (Optional)
        :param list name: claim name (Optional)
        :param list channel_id: claims in this channel (Optional)
        :param list not_channel_id: claims not in this channel (Optional)
        :param bool is_spent: only show spent txos (Optional)
        :param bool is_not_spent: only show not spent txos (Optional)
        :param bool is_my_input_or_output: txos which have your inputs or your outputs, if using this flag the other related flags are ignored (--is_my_output, --is_my_input, etc) (Optional)
        :param bool is_my_output: show outputs controlled by you (Optional)
        :param bool is_not_my_output: show outputs not controlled by you (Optional)
        :param bool is_my_input: show outputs created by you (Optional)
        :param bool is_not_my_input: show outputs not created by you (Optional)
        :param bool exclude_internal_transfers: excludes any outputs that are exactly this combination: "--is_my_input --is_my_output --type=other" this allows to exclude "change" payments, this flag can be used in combination with any of the other flags (Optional)
        :param str account_id: id of the account to query (Optional)
        :param str wallet_id: restrict results to specific wallet (Optional)
        :param int days_back: number of days back from today (not compatible with --start_day, --days_after, --end_day) (Optional)
        :param str start_day: start on specific date (YYYY-MM-DD) (instead of --days_back) (Optional)
        :param int days_after: end number of days after --start_day (instead of --end_day) (Optional)
        :param str end_day: end on specific date (YYYY-MM-DD) (instead of --days_after) (Optional)
        """
        __params_map = {'type': type,
                        'txid': txid,
                        'claim_id': claim_id,
                        'name': name,
                        'channel_id': channel_id,
                        'not_channel_id': not_channel_id,
                        'is_spent': is_spent,
                        'is_not_spent': is_not_spent,
                        'is_my_input_or_output': is_my_input_or_output,
                        'is_my_output': is_my_output,
                        'is_not_my_output': is_not_my_output,
                        'is_my_input': is_my_input,
                        'is_not_my_input': is_not_my_input,
                        'exclude_internal_transfers': exclude_internal_transfers,
                        'account_id': account_id,
                        'wallet_id': wallet_id,
                        'days_back': days_back,
                        'start_day': start_day,
                        'days_after': days_after,
                        'end_day': end_day}

        return self.make_request(SERVER_ADDRESS, 'txo_plot', __params_map, timeout=self.timeout)

    def txo_spend(self, type=None, txid=None, claim_id=None, channel_id=None, not_channel_id=None, name=None, is_my_input=None, is_not_my_input=None, exclude_internal_transfers=None, account_id=None, wallet_id=None, preview=None, blocking=None, batch_size=None, include_full_tx=None):
        """Spend transaction outputs, batching into multiple transactions as necessary.

        :param list type: claim type: stream, channel, support, purchase, collection, repost, other (Optional)
        :param list txid: transaction id of outputs (Optional)
        :param list claim_id: claim id (Optional)
        :param list channel_id: claims in this channel (Optional)
        :param list not_channel_id: claims not in this channel (Optional)
        :param list name: claim name (Optional)
        :param bool is_my_input: show outputs created by you (Optional)
        :param bool is_not_my_input: show outputs not created by you (Optional)
        :param bool exclude_internal_transfers: excludes any outputs that are exactly this combination: "--is_my_input --is_my_output --type=other" this allows to exclude "change" payments, this flag can be used in combination with any of the other flags (Optional)
        :param str account_id: id of the account to query (Optional)
        :param str wallet_id: restrict results to specific wallet (Optional)
        :param bool preview: do not broadcast the transaction (Optional)
        :param bool blocking: wait until abandon is in mempool (Optional)
        :param int batch_size: number of txos to spend per transactions (Optional)
        :param bool include_full_tx: include entire tx in output and not just the txid (Optional)
        """
        __params_map = {'type': type,
                        'txid': txid,
                        'claim_id': claim_id,
                        'channel_id': channel_id,
                        'not_channel_id': not_channel_id,
                        'name': name,
                        'is_my_input': is_my_input,
                        'is_not_my_input': is_not_my_input,
                        'exclude_internal_transfers': exclude_internal_transfers,
                        'account_id': account_id,
                        'wallet_id': wallet_id,
                        'preview': preview,
                        'blocking': blocking,
                        'batch_size': batch_size,
                        'include_full_tx': include_full_tx}

        return self.make_request(SERVER_ADDRESS, 'txo_spend', __params_map, timeout=self.timeout)

    def txo_sum(self, type=None, txid=None, claim_id=None, name=None, channel_id=None, not_channel_id=None, is_spent=None, is_not_spent=None, is_my_input_or_output=None, is_my_output=None, is_not_my_output=None, is_my_input=None, is_not_my_input=None, exclude_internal_transfers=None, account_id=None, wallet_id=None):
        """Sum of transaction outputs.

        :param list type: claim type: stream, channel, support, purchase, collection, repost, other (Optional)
        :param list txid: transaction id of outputs (Optional)
        :param list claim_id: claim id (Optional)
        :param list name: claim name (Optional)
        :param list channel_id: claims in this channel (Optional)
        :param list not_channel_id: claims not in this channel (Optional)
        :param bool is_spent: only show spent txos (Optional)
        :param bool is_not_spent: only show not spent txos (Optional)
        :param bool is_my_input_or_output: txos which have your inputs or your outputs, if using this flag the other related flags are ignored (--is_my_output, --is_my_input, etc) (Optional)
        :param bool is_my_output: show outputs controlled by you (Optional)
        :param bool is_not_my_output: show outputs not controlled by you (Optional)
        :param bool is_my_input: show outputs created by you (Optional)
        :param bool is_not_my_input: show outputs not created by you (Optional)
        :param bool exclude_internal_transfers: excludes any outputs that are exactly this combination: "--is_my_input --is_my_output --type=other" this allows to exclude "change" payments, this flag can be used in combination with any of the other flags (Optional)
        :param str account_id: id of the account to query (Optional)
        :param str wallet_id: restrict results to specific wallet (Optional)
        """
        __params_map = {'type': type,
                        'txid': txid,
                        'claim_id': claim_id,
                        'name': name,
                        'channel_id': channel_id,
                        'not_channel_id': not_channel_id,
                        'is_spent': is_spent,
                        'is_not_spent': is_not_spent,
                        'is_my_input_or_output': is_my_input_or_output,
                        'is_my_output': is_my_output,
                        'is_not_my_output': is_not_my_output,
                        'is_my_input': is_my_input,
                        'is_not_my_input': is_not_my_input,
                        'exclude_internal_transfers': exclude_internal_transfers,
                        'account_id': account_id,
                        'wallet_id': wallet_id}

        return self.make_request(SERVER_ADDRESS, 'txo_sum', __params_map, timeout=self.timeout)

    def utxo_list(self, account_id=None, wallet_id=None, page=None, page_size=None):
        """List unspent transaction outputs

        :param str account_id: id of the account to query (Optional)
        :param str wallet_id: restrict results to specific wallet (Optional)
        :param int page: page to return during paginating (Optional)
        :param int page_size: number of items on page during pagination (Optional)
        """
        __params_map = {'account_id': account_id,
                        'wallet_id': wallet_id,
                        'page': page,
                        'page_size': page_size}

        return self.make_request(SERVER_ADDRESS, 'utxo_list', __params_map, timeout=self.timeout)

    def utxo_release(self, account_id=None, wallet_id=None):
        """When spending a UTXO it is locally locked to prevent double spends;
occasionally this can result in a UTXO being locked which ultimately
did not get spent (failed to broadcast, spend transaction was not
accepted by blockchain node, etc). This command releases the lock
on all UTXOs in your account.

        :param str account_id: id of the account to query (Optional)
        :param str wallet_id: restrict operation to specific wallet (Optional)
        """
        __params_map = {'account_id': account_id,
                        'wallet_id': wallet_id}

        return self.make_request(SERVER_ADDRESS, 'utxo_release', __params_map, timeout=self.timeout)

    def wallet_add(self, wallet_id):
        """Add existing wallet.

        :param str wallet_id: wallet file name
        """
        __params_map = {'wallet_id': wallet_id}

        return self.make_request(SERVER_ADDRESS, 'wallet_add', __params_map, timeout=self.timeout)

    def wallet_balance(self, wallet_id=None, confirmations=None):
        """Return the balance of a wallet

        :param str wallet_id: balance for specific wallet (Optional)
        :param int confirmations: Only include transactions with this many confirmed blocks. (Optional)
        """
        __params_map = {'wallet_id': wallet_id,
                        'confirmations': confirmations}

        return self.make_request(SERVER_ADDRESS, 'wallet_balance', __params_map, timeout=self.timeout)

    def wallet_create(self, wallet_id, skip_on_startup=None, create_account=None, single_key=None):
        """Create a new wallet.

        :param str wallet_id: wallet file name
        :param bool skip_on_startup: don't add wallet to daemon_settings.yml (Optional)
        :param bool create_account: generates the default account (Optional)
        :param bool single_key: used with --create_account, creates single-key account (Optional)
        """
        __params_map = {'wallet_id': wallet_id,
                        'skip_on_startup': skip_on_startup,
                        'create_account': create_account,
                        'single_key': single_key}

        return self.make_request(SERVER_ADDRESS, 'wallet_create', __params_map, timeout=self.timeout)

    def wallet_decrypt(self, wallet_id=None):
        """Decrypt an encrypted wallet, this will remove the wallet password. The wallet must be unlocked to decrypt it

        :param str wallet_id: restrict operation to specific wallet (Optional)
        """
        __params_map = {'wallet_id': wallet_id}

        return self.make_request(SERVER_ADDRESS, 'wallet_decrypt', __params_map, timeout=self.timeout)

    def wallet_encrypt(self, new_password, wallet_id=None):
        """Encrypt an unencrypted wallet with a password

        :param str new_password: password to encrypt account
        :param str wallet_id: restrict operation to specific wallet (Optional)
        """
        __params_map = {'new_password': new_password,
                        'wallet_id': wallet_id}

        return self.make_request(SERVER_ADDRESS, 'wallet_encrypt', __params_map, timeout=self.timeout)

    def wallet_list(self, wallet_id=None, page=None, page_size=None):
        """List wallets.

        :param str wallet_id: show specific wallet only (Optional)
        :param int page: page to return during paginating (Optional)
        :param int page_size: number of items on page during pagination (Optional)
        """
        __params_map = {'wallet_id': wallet_id,
                        'page': page,
                        'page_size': page_size}

        return self.make_request(SERVER_ADDRESS, 'wallet_list', __params_map, timeout=self.timeout)

    def wallet_lock(self, wallet_id=None):
        """Lock an unlocked wallet

        :param str wallet_id: restrict operation to specific wallet (Optional)
        """
        __params_map = {'wallet_id': wallet_id}

        return self.make_request(SERVER_ADDRESS, 'wallet_lock', __params_map, timeout=self.timeout)

    def wallet_reconnect(self):
        """Reconnects ledger network client, applying new configurations.

        """
        __params_map = {}

        return self.make_request(SERVER_ADDRESS, 'wallet_reconnect', __params_map, timeout=self.timeout)

    def wallet_remove(self, wallet_id):
        """Remove an existing wallet.

        :param str wallet_id: name of wallet to remove
        """
        __params_map = {'wallet_id': wallet_id}

        return self.make_request(SERVER_ADDRESS, 'wallet_remove', __params_map, timeout=self.timeout)

    def wallet_send(self, wallet_id=None, change_account_id=None, funding_account_ids=None, preview=None, blocking=None):
        """Send the same number of credits to multiple addresses using all accounts in wallet to
fund the transaction and the default account to receive any change.

        :param str wallet_id: restrict operation to specific wallet (Optional)
        :param str change_account_id: account where change will go (Optional)
        :param str funding_account_ids: accounts to fund the transaction (Optional)
        :param bool preview: do not broadcast the transaction (Optional)
        :param bool blocking: wait until tx has synced (Optional)
        """
        __params_map = {'wallet_id': wallet_id,
                        'change_account_id': change_account_id,
                        'funding_account_ids': funding_account_ids,
                        'preview': preview,
                        'blocking': blocking}

        return self.make_request(SERVER_ADDRESS, 'wallet_send', __params_map, timeout=self.timeout)

    def wallet_status(self, wallet_id=None):
        """Status of wallet including encryption/lock state.

        :param str wallet_id: status of specific wallet (Optional)
        """
        __params_map = {'wallet_id': wallet_id}

        return self.make_request(SERVER_ADDRESS, 'wallet_status', __params_map, timeout=self.timeout)

    def wallet_unlock(self, password, wallet_id=None):
        """Unlock an encrypted wallet

        :param str password: password to use for unlocking
        :param str wallet_id: restrict operation to specific wallet (Optional)
        """
        __params_map = {'password': password,
                        'wallet_id': wallet_id}

        return self.make_request(SERVER_ADDRESS, 'wallet_unlock', __params_map, timeout=self.timeout)

